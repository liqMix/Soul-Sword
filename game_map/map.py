from data.load_inmates import InmateList
from entities.enemies import *
from entities.obstacles import *
from entities.item import *
from constants import *
import tcod.map
import tcod.path
import random
import numpy as np
import math


class GameMap:
    def __init__(self, size_x, size_y, num_rooms, player):
        # Map dimensions
        self.width = size_x
        self.height = size_y

        # Holds the vision and pathing logic
        self.tcod_map = tcod.map.Map(width=size_x, height=size_y)
        self.tcod_map.transparent[:] = False

        # Set up the map
        print('Initializing all cells to walls...')
        self.tiles = {}
        for i in range(self.width * self.height):
            self.tiles[i] = {'entity': Wall(idx_to_xy(i, size_x)),
                             'items': [],
                             'blocked': True}
        self.rooms = []
        self.hallways = []
        self.origin = (0, 0) # Origin is set when first room is generated
        for i in range(num_rooms):
            print("Generating room: ", i)
            self.rooms.append(self.gen_room())

        self.astar = tcod.path.AStar(self.tcod_map.walkable)
        # Initialize player
        print('Setting player position...')
        self.player = player
        self.player.set_pos(self.origin)
        self.tiles[xy_to_idx(self.player.x, self.player.y, self.width)]['entity'] = self.player
        self.entities = {'player':  self.player,
                         'items':   [],
                         'enemies': [],
                         'blocked': True}

        print('Generating initial view...')
        self.viewed = np.ndarray((self.width, self.height), dtype=bool)
        self.viewed[:] = False
        self.compute_fov(self.player.pos)

        print('Populating rooms with items...')
        self.populate()

    def gen_room(self):
        # If first room, set it at the
        if not self.rooms:
            min_d = ROOM['min_dim']
            max_d = ROOM['max_dim']
            w = int(random.randrange(min_d, max_d))
            h = int(random.randrange(min_d, max_d))
            (x, y) = (self.width // 2, self.height // 2)
            room = Room(x, y, w, h)
            self.origin = (room.x + w//2, room.y + h//2)
        else:
            room = self.add_room()

        for i in range(room.x, room.x2):
            for j in range(room.y, room.y2):
                self.tiles[xy_to_idx(i, j, self.width)] = {'entity': Ground((i, j)),
                                                           'blocked': False,
                                                           'items': []}
                self.tcod_map.walkable[j, i] = True
                self.tcod_map.transparent[j, i] = True

        return room

    def add_room(self):
        directions = ['N', 'E', 'W', 'S']
        direction = None

        # Create room
        min_d = ROOM['min_dim']
        max_d = ROOM['max_dim']
        room = None
        hallway = None

        while not self.area_free(room):
            # Create hallway
            hallway = None

            # Keep generating areas until an unoccupied one is found
            while not self.area_free(hallway):

                # Select origin room
                origin = random.choice(self.rooms)

                # Select a direction
                direction = random.choice(directions)
                side = origin.sides[direction]
                x = random.choice(side['x']) - 1
                y = random.choice(side['y']) - 1

                hallway_length = random.randrange(HALLWAY['min_length'], HALLWAY['max_length'])
                hallway_width = HALLWAY['width']
                hallway = Room(x, y, hallway_width, hallway_length, direction)

            # Set direction
            side = hallway.sides[direction]
            x = random.choice(side['x'])
            y = random.choice(side['y'])

            w = int(random.randrange(min_d, max_d))
            h = int(random.randrange(min_d, max_d))
            room = Room(x, y, w, h, direction)

        self.hallways.append(hallway)
        for i in range(hallway.x, hallway.x2):
            for j in range(hallway.y, hallway.y2):
                self.tiles[xy_to_idx(i, j, self.width)] = {'entity': Ground((i, j)),
                                                           'blocked': False,
                                                           'items': []}
                self.tcod_map.walkable[j, i] = True
                self.tcod_map.transparent[j, i] = True
        return room

    # Checks if the area is unoccupied
    def area_free(self, room=None):
        if not room:
            return False
        if room.x2 >= self.width or room.x < 0:
            return False
        if room.y2 >= self.height or room.y < 0:
            return False

        for i in range(room.x, room.x2):
            for j in range(room.y, room.y2):
                if self.tiles[xy_to_idx(i, j, self.width)]['entity'].type is not 'wall':
                    return False

        return True

    # Check is move to destination is legal for entity
    def check_move(self, move, entity):
        dest_x, dest_y = move
        dest_x = entity.x + dest_x
        dest_y = entity.y + dest_y

        # Check bounds of map
        if (dest_x >= self.width) or (dest_x < 0):
            return False
        elif (dest_y >= self.height) or (dest_y < 0):
            return False

        # Check if currently occupied
        elif self.tiles[xy_to_idx(dest_x, dest_y, self.width)]['blocked']:
            return False

        # Find walkable path to destination
        elif self.astar.get_path(entity.y, entity.x, dest_y, dest_x) is None:
            return False

        return True

    # Add items to entity
    def get_items(self, entity):
        idx = xy_to_idx(entity.x, entity.y, self.width)
        items_to_get = self.tiles[idx]['items']
        if items_to_get:
            entity.add_items(items_to_get)
            self.tiles[idx]['items'] = []
            for item in items_to_get:
                self.entities['items'].remove(item)

    # Add entities and items to map
    def populate(self):
        # add items
        for item in ITEMS.keys():

            idx = None
            while idx is None or self.tiles[idx]['entity'].type is not 'ground':
                rand_x = math.floor(np.random.random() * self.width)
                rand_y = math.floor(np.random.random() * self.height)
                idx = xy_to_idx(rand_x, rand_y, self.width)

            new_item = Item(item, (rand_x, rand_y))
            self.tiles[idx]['items'].append(new_item)
            self.entities['items'].append(new_item)

        # add enemies
        num_enemies = random.randrange(ROOM['min_enemies'], ROOM['max_enemies'])
        enemies = InmateList(num_enemies)
        for enemy in enemies.inmate_list:

            idx = None
            while idx is None or (self.tiles[idx]['blocked'] or self.tiles[idx]['entity'].type is not 'ground'):
                rand_x = math.floor(np.random.random() * self.width)
                rand_y = math.floor(np.random.random() * self.height)
                idx = xy_to_idx(rand_x, rand_y, self.width)

            new_enemy = Enemy(inmate=enemy)
            new_enemy.set_pos((rand_x, rand_y))
            self.entities['enemies'].append(new_enemy)
            self.tiles[idx]['entity'] = new_enemy
            self.tiles[idx]['blocked'] = True

    # Update cells
    def update_cell(self, entity):
        prev_x, prev_y = entity.prev_pos
        prev_tile = self.tiles[xy_to_idx(prev_x, prev_y, self.width)]
        new_tile = self.tiles[xy_to_idx(entity.x, entity.y, self.width)]
        prev_tile['entity'] = Ground((prev_x, prev_y))
        prev_tile['blocked'] = False
        new_tile['entity'] = entity
        new_tile['blocked'] = True

    # Adds viewable cells to viewed history
    # and sets fov cells
    def compute_fov(self, pos):
        x, y = pos
        radius = PLAYER['fov_radius']
        self.tcod_map.compute_fov(x, y, radius, light_walls=True, algorithm=tcod.FOV_RESTRICTIVE)
        self.viewed |= self.tcod_map.fov

    # Move all enemies
    def move_enemies(self):
        for enemy in self.entities['enemies']:
            if self.tcod_map.fov[enemy.y, enemy.x]:
                path = self.astar.get_path(enemy.y, enemy.x, self.player.y, self.player.x)
                if path:
                    move = (path[0][1] - enemy.x, path[0][0] - enemy.y)
                    if self.check_move(move, enemy):
                        enemy.move(move)
                        self.update_cell(enemy)


class Room:
    def __init__(self, x=0, y=0, w=0, h=0, direction=None):
        if direction:
            if direction is 'N':
                self.x = x
                self.y = y
                self.x2 = x + w
                self.y2 = y + h
            if direction is 'S':
                self.x2 = x
                self.y2 = y
                self.x = self.x2 - w
                self.y = self.y2 - h
            elif direction is 'E':
                self.x = x
                self.y = y
                self.x2 = self.x + h
                self.y2 = self.y + w
            elif direction is 'W':
                self.x2 = x
                self.y = y
                self.x = self.x2 - w
                self.y2 = self.y + h
        else:
            self.x = x
            self.y = y
            self.x2 = x+w
            self.y2 = y+h

        self.sides = {
            'S': {'x': range(self.x+1, self.x2-1), 'y': [self.y+1]},
            'N': {'x': range(self.x+1, self.x2-1), 'y': [self.y2-1]},
            'W': {'x': [self.x+1], 'y': range(self.y+1, self.y2-1)},
            'E': {'x': [self.x2-1], 'y': range(self.y+1, self.y2-1)}
        }
