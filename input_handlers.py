import tcod.event
import tcod.event_constants as keys
UP_KEYS = [keys.K_w, keys.K_UP]
DOWN_KEYS = [keys.K_s, keys.K_DOWN]
RIGHT_KEYS = [keys.K_d, keys.K_RIGHT]
LEFT_KEYS = [keys.K_a, keys.K_LEFT]


# Returns dict containing result
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


    # System
    if symbol == keys.K_ESCAPE:
        return {'exit': True}
    elif (symbol == keys.K_RETURN) and (modifiers % tcod.event.KMOD_ALT):
        return {'fullscreen': True}

    return {}


def handle_mouse(mouse):
    return {}
