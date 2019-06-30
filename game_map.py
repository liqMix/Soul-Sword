import tcod.map
import tcod.path
import tcod.random
from item import *
from window import *
import numpy as np
import math


class GameMap(Frame):
    def __init__(self, center=(0, 0), size_x=50, size_y=30, player=None):
        super(GameMap, self).__init__(center=center, size=(size_x, size_y), name='gamemap')
        self.map = tcod.map.Map(width=size_x, height=size_y)
        self.view_x = 80
        self.view_y = 24
        self.top_left_x = self.x - (self.view_x // 2)
        self.top_left_y = self.y - (self.view_y // 2)

        self.cells = [x for x in range(self.size)]

        for i in range(self.size):
            self.cells[i] = {'entity':   None,
                             'items':    []}

        self.player = player
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

        idx = xy_to_idx(entity.x, entity.y, self.width)
        items_to_get = self.cells[idx]['items']
        if items_to_get:
            entity.add_items(items_to_get)
            self.cells[idx]['items'] = []
            for item in items_to_get:
                self.entities['items'].remove(item)

    # Add items to map
    def populate(self):
        for item in ITEMS.keys():
            rand_x = math.floor(np.random.random() * self.width)
            rand_y = math.floor(np.random.random() * self.height)
            new_item = Item(item, (rand_x, rand_y))
            idx = xy_to_idx(rand_x, rand_y, self.width)
            self.cells[idx]['items'].append(new_item)
            self.entities['items'].append(new_item)

    # Update cells
    def update_cells(self):
        prev_x, prev_y = self.player.prev_pos
        self.cells[xy_to_idx(prev_x, prev_y, self.width)]['entity'] = None
        self.cells[xy_to_idx(self.player.x, self.player.y, self.width)]['entity'] = self.player

        for e in self.entities['enemies']:
            prev_x, prev_y = self.e.prev_pos
            self.cells[xy_to_idx(prev_x, prev_y, self.width)]['entity'] = None
            self.cells[xy_to_idx(e.x, e.y, self.width)]['entity'] = e

    # Draw map to screen
    def draw(self, con):
        self.update_cells()
        top_edge = self.top_left_y
        bot_edge = self.top_left_y + self.view_y
        left_edge = self.top_left_x
        right_edge = self.top_left_x + self.view_x

        half_width = self.view_x // 2
        half_height = self.view_y // 2

        # The cells to draw
        cells_x_range = range(self.player.x - half_width, self.player.x + half_width)
        cells_y_range = range(self.player.y - half_height, self.player.y + half_height)

        for y in cells_y_range:
            if 0 <= y < self.height:
                for x in cells_x_range:
                    if 0 <= x < self.width:
                        idx = xy_to_idx(x, y, self.width)
                        rel_x = x - self.player.x
                        rel_y = y - self.player.y
                        cell = self.cells[idx]
                        item = cell['items']
                        entity = cell['entity']

                        if entity:
                            if entity.type is 'player':
                                entity.draw(con, self.x, self.y)
                            else:
                                entity.draw(con, rel_x + self.x, rel_y + self.y)

                        elif item:
                            item[0].draw(con, rel_x + self.x, rel_y + self.y)
                        else:
                            con.put_char(rel_x + self.x, rel_y + self.y, ord('-'), tcod.BKGND_NONE)

        # Draw border of map
        view_edge_symbol = ord('#')
        for x in range(self.view_x+1):
            con.put_char(x + left_edge, top_edge, view_edge_symbol, tcod.BKGND_NONE)
            con.put_char(x + left_edge, bot_edge, view_edge_symbol, tcod.BKGND_NONE)

        for y in range(self.view_y):
            con.put_char(left_edge, y + top_edge, view_edge_symbol, tcod.BKGND_NONE)
            con.put_char(right_edge, y + top_edge, view_edge_symbol, tcod.BKGND_NONE)
