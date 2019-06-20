from entity import *


class Player(Entity):
    def __init__(self, center):
        super(Player, self).__init__(center)
        self.name = "Player"
