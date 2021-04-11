from entities.entity import *
from constants import *


class Item(Entity):
    def __init__(self, item_name='Nothing', center=(0, 0)):
        super(Item, self).__init__(center, name=item_name)
        self.hp = 0
        self.type = 'item'
        self.name = item_name
        try:
            info = ITEMS[self.name]
            self.stats = info['stats']
            self.symbol = info['symbol']
            self.desc = info['desc']
            self.subtype = info['type']
            self.color = COLORS[self.subtype]
        except KeyError:
            pass


class Soul(Item):
    def __init__(self, stats, name, center=(0, 0)):
        super(Soul, self).__init__(name, center)
        self.stats = stats
        self.name = name + '\'s Soul'
        self.subtype = 'soul'
        self.symbol = 'S'
        self.desc = 'The soul of the late ' + name + '.'
        self.stats = stats
        self.color = COLORS[self.subtype]
