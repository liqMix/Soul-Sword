import tcod


class Entity:
    def __init__(self, center, name=None, symbol=' '):
        self.name = name
        self.color = tcod.white
        self.pos = center
        self.prev_pos = (0, 0)
        self.symbol = symbol
        self.hp = 100
        self.weapon = "None"
        self.inventory = []
        self.x, self.y = self.pos
        self.controller = None

    def move(self, move):
        dx, dy = move
        self.set_pos((self.x+dx, self.y+dy))

    def draw(self, con):
        #con.put_char(self.x, self.y,
        #             ord(self.symbol),
        #             tcod.BKGND_NONE)
        tcod.console_put_char_ex(con, self.x, self.y, self.symbol, fore=self.color, back=con.default_bg)

    def set_pos(self, pos):
        self.prev_pos = self.pos
        self.x, self.y = pos
        self.pos = pos

    def add_items(self, items):
        for item in items:
            self.inventory.append(item)
