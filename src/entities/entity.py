import tcod

from handlers.message import MessageHandler


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
        self.level = 1
        self.weapon = "None"
        self.inventory = []
        self.stats = {
            'str': 0,
            'int': 100,
            'con': 0,
            'def': 0,
            'agi': 0
        }

        self.current_hp = 0
        self.total_hp = 0
        self.view = None
        self.view_radius = 0

        self.weapon = 'fists'

    def update_stat(self, stat, change):
        self.stats[stat] += change
        if stat == 'con':
            self.total_hp = self.stats[stat] * 10
            if self.total_hp == 0:
                self.total_hp = 10
        elif stat == 'int':
            self.view_radius = (self.stats[stat] // 5) + 2

    def move(self, move):
        dx, dy = move
        self.set_pos((self.x + dx, self.y + dy))

    def draw(self, con, x, y):
        tcod.console_put_char_ex(
            con,
            x,
            y,
            self.symbol,
            fore=self.color, back=con.default_bg
        )

    def set_pos(self, pos):
        self.prev_pos = self.pos
        self.x, self.y = pos
        self.pos = pos

    def add_items(self, items):
        for item in items:
            self.inventory.append(item)
            MessageHandler.create_message('Picked up ' + item.name + '!', item.color)

    def update_fov(self, tcod_map):
        x, y = self.pos
        tcod_map.compute_fov(x, y, self.view_radius, light_walls=True, algorithm=tcod.FOV_RESTRICTIVE)
        self.view = tcod_map.fov
