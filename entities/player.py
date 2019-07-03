from entities.entity import *


class Player(Entity):
    def __init__(self, pos=(0, 0), controller=None):
        super(Player, self).__init__(pos, 'Player', '@', controller)
        self.type = 'player'
        self.color = tcod.amber
        self.desc = "The player"

    def move(self, move):
        super(Player, self).move(move)
        self.controller.increment_ticks(1)
