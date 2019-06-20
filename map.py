import tcod.map
import tcod.path
import tcod.random
from item import *
import numpy as np
import math

class Map():
    def __init__(self, center, size_x=32, size_y=32):
        self.map = tcod.map.Map(width=size_x, height=size_y)
        self.items = []
        self.enemies = []
        self.size_x = size_x // 2
        self.size_y = size_y // 2
        self.pos_x, self.pos_y = center

        self.populate()

    def check_move(self, move, entity):
        x, y = move
        x = entity.pos_x + x
        y = entity.pos_y + y

        astar = tcod.path.AStar(self.map.walkable)
        if astar.get_path(entity.pos_x, entity.pos_y, x, y) is None:
            return False

        elif (x > (self.pos_x + self.size_x)) or (x < (self.pos_x - self.size_x)):
            return False

        elif (y > (self.pos_y + self.size_y)) or (y < (self.pos_y - self.size_y)):
            return False

        return True

    def get_items(self, loc):
        picked_up = []
        for item in self.items:
            if item.pos == loc:
                picked_up.append(self.items.pop(self.items.index(item)))

        return picked_up

    def populate(self):
        rand_x = math.floor(np.random.random() * (self.size_x-1)) + 1 + self.pos_x
        rand_y = math.floor(np.random.random() * (self.size_y-1)) + 1 + self.pos_y
        self.items.append(Item((rand_x, rand_y), "Potion"))

    def draw(self, con):
        top_edge_y = self.pos_y - self.size_y - 1
        bot_edge_y = self.pos_y + self.size_y + 1
        left_edge_x = self.pos_x - self.size_x - 1
        right_edge_x = self.pos_x + self.size_x + 1

        for x in range(self.size_x*2 + 2):
            tcod.console_put_char(con, x + left_edge_x, top_edge_y, '#', tcod.BKGND_NONE)
            tcod.console_put_char(con, x + left_edge_x, bot_edge_y, '#', tcod.BKGND_NONE)
        for y in range(self.size_y*2 + 3):
            tcod.console_put_char(con, left_edge_x, y + top_edge_y, '#', tcod.BKGND_NONE)
            tcod.console_put_char(con, right_edge_x, y + top_edge_y, '#', tcod.BKGND_NONE)

        for item in self.items:
            tcod.console_put_char(con, item.pos_x, item.pos_y, item.info['symbol'], tcod.BKGND_NONE)
