import tcod


class Entity:
    def __init__(self, pos=(0, 0), name=None, symbol=' ', controller=None, color=tcod.white):
        self.name = name
        self.color = tcod.white
        self.pos = pos
        self.x, self.y = self.pos
        self.prev_pos = pos
        self.symbol = symbol
        self.color = color
        self.controller = controller
        self.hp = 100
        self.level = 1
        self.weapon = "None"
        self.inventory = []

    def move(self, move):
        dx, dy = move
        self.set_pos((self.x+dx, self.y+dy))

    def draw(self, con, x, y):
        tcod.console_put_char_ex(con,
                                 x,
                                 y,
                                 self.symbol,
                                 fore=self.color, back=con.default_bg)

    def set_pos(self, pos):
        self.prev_pos = self.pos
        self.x, self.y = pos
        self.pos = pos

    def add_items(self, items):
        for item in items:
            self.inventory.append(item)
            if self.controller:
                self.controller.messages.add_message('Picked up ' + item.name + '!')
