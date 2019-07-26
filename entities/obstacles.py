from entities.entity import Entity
import tcod


class Wall(Entity):
    def __init__(self, pos=(0, 0)):
        super(Wall, self).__init__(pos, 'Wall', '[', color=tcod.grey)
        self.type = 'obstacle'
