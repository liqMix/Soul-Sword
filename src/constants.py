import tcod
import yaml

# Holds game-wide constants

# SYSTEM #
SCREEN_WIDTH = 100
SCREEN_HEIGHT = 80


# ITEMS #
ITEM_DEF = "resources/items.yaml"
with open(ITEM_DEF) as file:
    ITEMS = yaml.safe_load(file)


# COLORS #
COLORS = {'player':       tcod.amber,
          'enemy':        tcod.red,
          'consumable':   tcod.pink,
          'usable':       tcod.green,
          'resource':     tcod.purple,
          'soul':         tcod.celadon,
          'equip':        tcod.blue,
          'dark_wall':    tcod.darker_gray,
          'dark_ground':  tcod.darker_gray,
          'light_wall':   tcod.light_gray,
          'light_ground': tcod.light_gray}

# SYMBOLS #
SYMBOLS = {'player':    '@',
           'wall':      '#',
           'ground':    '.',
           'enemy':     'E',
           'item':      ''}

# GAME MAP #
GAMEMAP = {'size_x': 500,
           'size_y': 500}

# ROOMS #
ROOM = {'min_rooms': 25,
        'max_rooms': 40,
        'min_enemies': 5,
        'max_enemies': 10,
        'min_dim': 5,
        'max_dim': 20}

# HALLWAYS #
HALLWAY = {'width': 3,
           'min_length': 3,
           'max_length': 10}

# PLAYER #
PLAYER = {'fov_radius': 5}

# MESSAGE WINDOW #
MESSAGES = {'width': int(SCREEN_WIDTH // 1.25),
            'height': int(SCREEN_HEIGHT // 4),
            'max_lines': 9}

# MUGSHOT #
MUGSHOT = {'scale_factor': 0.05,
           'intensity_correction': 1.75,
           'width_correction': 5/4,
           'x_pos': int(SCREEN_WIDTH // 1.75),
           'y_pos': int(SCREEN_HEIGHT // 30)}

# COMBAT #
COMBAT = {'min_hit_chance': 0.25,
          'max_hit_chance': 0.95,
          'base_hit_chance': 0.5,
          'hit_chance_per_diff': 0.1}