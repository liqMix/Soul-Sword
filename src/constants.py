import tcod
import yaml
import configparser

# Loads and sets game constants from resources and configuration files
config = configparser.RawConfigParser()
config.read('configuration.ini')


def config_to_obj(section):
    obj = {}
    for key in config[section].keys():
        try:
            val = config.getint(section, key)
        except Exception as e:
            try:
                val = config.getfloat(section, key)
            except Exception as e:
                val = config.get(section, key)
        obj[key] = val
    return obj


# SCREEN #
SCREEN = config_to_obj('SCREEN')
SCREEN_WIDTH = SCREEN['width']
SCREEN_HEIGHT = SCREEN['height']

# ITEMS #
ITEM_DEF = "resources/items.yaml"
with open(ITEM_DEF) as file:
    ITEMS = yaml.safe_load(file)


# COLORS #
COLORS = {
    'player':       tcod.amber,
    'enemy':        tcod.red,
    'consumable':   tcod.pink,
    'usable':       tcod.green,
    'resource':     tcod.purple,
    'soul':         tcod.celadon,
    'equip':        tcod.blue,
    'dark_wall':    tcod.darker_gray,
    'dark_ground':  tcod.darker_gray,
    'light_wall':   tcod.light_gray,
    'light_ground': tcod.light_gray
}

# SYMBOLS #
SYMBOLS = config_to_obj('SYMBOL')

# GAME MAP #
GAMEMAP = config_to_obj('MAP')

# ROOMS #
ROOM = config_to_obj('ROOM')

# HALLWAYS #
HALLWAY = config_to_obj('HALLWAY')

# PLAYER #
PLAYER = config_to_obj('PLAYER')

# MESSAGE WINDOW #
MESSAGES = config_to_obj('MESSAGES')

# MUGSHOT #
MUGSHOT = config_to_obj('MUGSHOT')

# COMBAT #
COMBAT = config_to_obj("COMBAT")
