import tcod.map
import tcod.path
import tcod.random
from item import *
from window import *
import numpy as np
import math


class GameMap(Frame):
    def __init__(self, anchor=(0, 0), size_x=500, size_y=500, player=None):
        super(GameMap, self).__init__(anchor=anchor, name='gamemap')
        self.map = tcod.map.Map(width=size_x, height=size_y)
        self.width = size_x
        self.height = size_y
        self.view_x = 80
        self.view_y = 24
        self.top_left = (self.x - self.view_x, self.y - self.view_y)

        self.cells = [x for x in range(size_x * size_y)]

        for i in range(len(self.cells)):
            self.cells[i] = {'entity': None,
                             'items':    []}

        self.player = player
        self.player.x = self.width//2
        self.player.y = self.height//2
        self.cells[xy_to_1d(self.player.x, self.player.y, self.width)]['entity'] = self.player
        self.entities = {'player':  self.player,
                         'items':   [],
                         'enemies': []}

        self.populate()

    # Check is move to destination is legal for entity
    def check_move(self, move, entity):
        dest_x, dest_y = move
        dest_x = entity.x + dest_x
        dest_y = entity.y + dest_y

        # Find walkable path to destination
        astar = tcod.path.AStar(self.map.walkable)
        if astar.get_path(entity.x, entity.y, dest_x, dest_y) is None:
            return False

        elif (dest_x >= self.width) or (dest_x < 0):
            return False

        elif (dest_y >= self.height) or (dest_y < 0):
            return False

        return True

    # Return list of items and remove from map
    def get_items(self, entity):

        # Get relative position of entity
        x, y = entity.pos
        idx = xy_to_1d(x, y, self.width)

        items_to_get = self.cells[idx]['items']
        if items_to_get is not None:
            entity.add_items(items_to_get)
            self.cells[idx]['items'] = []

    # Add items to map
    def populate(self):
        for item in ITEMS.keys():
            rand_x = math.floor(np.random.random() * (self.width - 1) + 1)
            rand_y = math.floor(np.random.random() * (self.height - 1) + 1)
            new_item = Item(item, (rand_x, rand_y))
            print(xy_to_1d(rand_x, rand_y, self.width))
            self.cells[xy_to_1d(rand_x, rand_y, self.width)]['items'].append(new_item)

    # Draw map to screen
    def draw(self, con):
        view_width = self.view_x
        view_height = self.view_y
        top_edge_y = self.y - view_height - 1
        bot_edge_y = self.y + view_height + 1
        left_edge_x = self.x - view_width - 1
        right_edge_x = self.x + view_width + 1

        # Draw border of map
        view_edge_symbol = ord('#')
        for x in range(view_width + 2):
            con.put_char(x + left_edge_x, top_edge_y, view_edge_symbol, tcod.BKGND_NONE)
            con.put_char(x + left_edge_x, bot_edge_y, view_edge_symbol, tcod.BKGND_NONE)

        for y in range(view_height + 3):
            con.put_char(left_edge_x, y + top_edge_y, view_edge_symbol, tcod.BKGND_NONE)
            con.put_char(right_edge_x, y + top_edge_y, view_edge_symbol, tcod.BKGND_NONE)

        view_x_range = range(self.player.x - (view_width//2), self.player.x + (view_width//2))
        view_y_range = range(self.player.y - (view_height//2), self.player.y + (view_height//2))
        view_size = view_width * view_height

        for x in view_x_range:
            for y in view_y_range:
                idx = xy_to_1d(x, y, self.width)
                if idx < 0 or idx >= view_size:
                    pass
                else:
                    item = self.cells[idx]['items']
                    entity = self.cells[idx]['entity']
                    if entity is not None:
                        entity.draw(con, x+left_edge_x, y+top_edge_y)
                    elif item:
                        item[0].draw(con, x+left_edge_x, y+top_edge_y)
                    else:
                        con.put_char(x+left_edge_x, y+top_edge_y, ord('-'), tcod.BKGND_NONE)
