from entity import *


class Player(Entity):
    def __init__(self, center, controller):
        super(Player, self).__init__(center, name='Player', symbol='@')
        self.name = "Player"
        self.color = tcod.amber
        self.controller = controller

    def move(self, move):
        super(Player, self).move(move)
        self.controller.increment_ticks(1)
