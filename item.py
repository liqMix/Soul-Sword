from entity import *
from constants import *


class Item(Entity):
    def __init__(self, item_name='Nothing', center=(0, 0)):
        super(Item, self).__init__(center, name=item_name)
        self.hp = 0
        self.type = 'item'
        self.name = item_name
        info = ITEMS[self.name]
        self.symbol = info['symbol']
        self.desc = info['desc']
