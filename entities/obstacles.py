from entities.entity import Entity
from constants import COLORS, SYMBOLS
import tcod


class Wall(Entity):
    def __init__(self, pos=(0, 0)):
        super(Wall, self).__init__(pos, 'Wall', symbol=SYMBOLS['wall'], color=COLORS['light_wall'])
        self.type = 'wall'

    def draw_darker(self, *args):
        self.color = COLORS['dark_wall']
        self.draw(*args)
        self.color = COLORS['light_wall']


class Ground(Entity):
    def __init__(self, pos=(0, 0)):
        super(Ground, self).__init__(pos, 'Ground', symbol=SYMBOLS['ground'], color=COLORS['light_ground'])
        self.type = 'ground'

    def draw_darker(self, *args):
        self.color = COLORS['dark_ground']
        self.draw(*args)
        self.color = COLORS['light_ground']