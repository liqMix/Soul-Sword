from entities.entity import *
from constants import *


class Player(Entity):
    def __init__(self, pos=(0, 0), controller=None):
        super(Player, self).__init__(pos, 'Player', '@', controller)
        self.type = 'player'
        self.color = COLORS['player']
        self.desc = "The player"

        for key in self.stats.keys():
            self.update_stat(key, 10)

        self.current_hp = self.total_hp
        self.view_history = None

    def move(self, move):
        super(Player, self).move(move)

    def set_view(self, view):
        self.view_history = view

    def update_fov(self, tcod_map):
        x, y = self.pos
        tcod_map.compute_fov(x, y, self.view_radius, light_walls=True, algorithm=tcod.FOV_RESTRICTIVE)
        self.view = tcod_map.fov
        self.view_history |= self.view
