from entity import *
ITEMS = {"Potion": {"symbol": "P", "desc": "Heals your health like you'd expect it to. (10%)"}}


class Item(Entity):
    def __init__(self, center, item_name):
        super(Item, self).__init__(center)
        self.hp = 0
        self.name = item_name
        self.info = ITEMS[self.name]