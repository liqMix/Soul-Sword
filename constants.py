import tcod

# Holds game-wide constants
#   These will eventually be read from an external text file
#

# SYSTEM #
SCREEN_WIDTH = 100
SCREEN_HEIGHT = 80


# ITEMS #
ITEMS = {"Potion": {"symbol": "P",
                    'type': 'consumable',
                    "desc": "Heals your health like you'd expect it to. (10%)"},

         "Sword":  {"symbol": "|",
                    'type': 'equip',
                    "desc": "Wow cool! Nice. Careful!"},

         "Nothing":   {"symbol": "n",
                       'type': 'consumable',
                       "desc": "Truly one of a kind."}}


# COLORS #
COLORS = {'player':     tcod.amber,
          'enemy':      tcod.red,
          'consumable': tcod.pink,
          'equip':      tcod.blue}


# UTILITY #
def xy_to_idx(x, y, width):
    return x + (y*width)
