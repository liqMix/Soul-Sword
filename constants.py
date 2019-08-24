import tcod

# Holds game-wide constants

# SYSTEM #
SCREEN_WIDTH = 100
SCREEN_HEIGHT = 80


# ITEMS #
ITEMS = {'Potion':  {'symbol': 'P',
                     'type': 'consumable',
                     'desc': 'Heals your health like you\'d expect it to. (10%)',
                     'min': 1,
                     'max': 10},

         'Sword':   {'symbol': '|',
                     'type': 'equip',
                     'desc': 'Wow cool! Nice. Careful!',
                     'min': 1,
                     'max': 3},

         'Nothing': {'symbol': 'n',
                     'type': 'consumable',
                     'desc': 'Truly one of a kind.',
                     'min': 1,
                     'max': 2},

         'Roster':  {'symbol': 'r',
                     'type': 'usable',
                     'desc': 'Contains a list of all enemies on this floor.',
                     'min': 1,
                     'max': 2},

         'Stone':   {'symbol': 's',
                     'type': 'resource',
                     'desc': 'It\'s a rock.',
                     'min': 1,
                     'max': 20}
         }


# COLORS #
COLORS = {'player':       tcod.amber,
          'enemy':        tcod.red,
          'consumable':   tcod.pink,
          'usable':       tcod.green,
          'resource':     tcod.purple,
          'equip':        tcod.blue,
          'dark_wall':    tcod.darker_gray,
          'dark_ground':  tcod.darker_gray,
          'light_wall':   tcod.light_gray,
          'light_ground': tcod.light_gray,}

# SYMBOLS #
SYMBOLS = {'player':    '@',
           'wall':      '#',
           'ground':    '.',
           'enemy':     'E',
           'item':      ''}
# ROOMS #
ROOM = {'min_rooms': 25,
        'max_rooms': 40,
        'min_enemies': 10,
        'max_enemies': 25,
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
# UTILITY #


def xy_to_idx(x, y, width):
    return x + (y*width)


def idx_to_xy(idx, width):
    y = idx % width
    x = idx - y
    return (x, y)



