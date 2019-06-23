import tcod.event
import tcod.event_constants as keys


# Maps an input key to a movement value
class KeysToMove:
    def __init__(self):
        self.key_map = {
                       'UP_KEY': [keys.K_w, keys.K_UP, keys.K_KP_8],
                       'DOWN_KEY': [keys.K_s, keys.K_DOWN, keys.K_KP_2],
                       'RIGHT_KEY': [keys.K_d, keys.K_RIGHT, keys.K_KP_6],
                       'LEFT_KEY': [keys.K_a, keys.K_LEFT, keys.K_KP_4],
                       'UP_LEFT_KEY': [keys.K_q, keys.K_KP_7],
                       'UP_RIGHT_KEY': [keys.K_e, keys.K_KP_9],
                       'DOWN_LEFT_KEY': [keys.K_z, keys.K_KP_1],
                       'DOWN_RIGHT_KEY': [keys.K_c, keys.K_KP_3]
                       }

        self.move_map = {
                        'UP_KEY': (0, -1),
                        'DOWN_KEY': (0, 1),
                        'RIGHT_KEY': (1, 0),
                        'LEFT_KEY': (-1, 0),
                        'UP_LEFT_KEY': (-1, -1),
                        'UP_RIGHT_KEY': (1, -1),
                        'DOWN_LEFT_KEY': (-1, 1),
                        'DOWN_RIGHT_KEY': (1, 1)
                        }

    def key_to_move(self, symbol):
        for key, value in self.key_map.items():
            if symbol in value:
                return self.move_map[key]
        return None


# Initializes the class
key_mapper = KeysToMove()


# Returns dict containing result
def handle_keys(key):
    type = key.type
    symbol = key.sym
    mod = key.mod

    # Movement
    movement = key_mapper.key_to_move(symbol)
    if key_mapper.key_to_move(symbol) is not None:
        return {'move': movement}

    # Menus
    if symbol is keys.K_i:
        return {'toggle': 'inventory'}

    # System
    if symbol == keys.K_ESCAPE:
        return {'exit': True}
    elif (symbol == keys.K_RETURN) and (mod & tcod.event.KMOD_ALT):
        return {'fullscreen': True}

    return {}

def handle_mouse(mouse):
    return {}
