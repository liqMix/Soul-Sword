
class Entity():
    def __init__(self, center):
        self.name = None
        self.pos = center
        self.hp = 100
        self.weapon = "None"
        self.inventory = []
        self.pos_x, self.pos_y = self.pos

    def move(self, move):
        dx, dy = move
        self.pos_x += dx
        self.pos_y += dy
        self.pos = (self.pos_x, self.pos_y)

    def add_items(self, items):
        for item in items:
            self.inventory.append(item)