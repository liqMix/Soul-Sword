from entities.obstacles import *
from constants import idx_to_xy


def initialize_map(size, width):
    cells = [x for x in range(size)]
    for i in range(len(cells)):
        cells[i] = {'entity': Wall(idx_to_xy(i, width)),
                    'items': []}
    return cells


class Room:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.x2 = x+w
        self.y2 = y+h
