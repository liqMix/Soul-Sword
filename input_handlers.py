import tcod.event
import tcod.event_constants as keys
UP_KEYS = [keys.K_w, keys.K_UP, keys.K_KP_8]
DOWN_KEYS = [keys.K_s, keys.K_DOWN, keys.K_KP_2]
RIGHT_KEYS = [keys.K_d, keys.K_RIGHT, keys.K_KP_6]
LEFT_KEYS = [keys.K_a, keys.K_LEFT, keys.K_KP_4]
UP_LEFT_KEYS = [keys.K_q, keys.K_KP_7]
UP_RIGHT_KEYS = [keys.K_e, keys.K_KP_9]
DOWN_LEFT_KEYS = [keys.K_z, keys.K_KP_1]
DOWN_RIGHT_KEYS = [keys.K_c, keys.K_KP_3]


# Returns dict containing result
# TODO: make less ugly
def handle_keys(key):
    type = key.type
    symbol = key.sym
    modifiers = key.mod
    
    # Movement
    if symbol in UP_KEYS:
        return {'move': (0, -1)}
    elif symbol in DOWN_KEYS:
        return {'move': (0, 1)}
    elif symbol in RIGHT_KEYS:
        return {'move': (1, 0)}
    elif symbol in LEFT_KEYS:
        return {'move': (-1, 0)}
    elif symbol in UP_RIGHT_KEYS:
        return {'move': (1, -1)}
    elif symbol in UP_LEFT_KEYS:
        return {'move': (-1, -1)}
    elif symbol in DOWN_RIGHT_KEYS:
        return {'move': (1, 1)}
    elif symbol in DOWN_LEFT_KEYS:
        return {'move': (-1, 1)}

    if symbol is keys.K_i:
        return {'toggle': 'inventory'}
    # System
    if symbol == keys.K_ESCAPE:
        return {'exit': True}
    elif (symbol == keys.K_RETURN) and (modifiers % tcod.event.KMOD_ALT):
        return {'fullscreen': True}

    return {}


def handle_mouse(mouse):
    return {}
