from definitions.enums import Action, Movement
from tcod.event import KMOD_ALT


# Initializes the class
class InputHandler:

    @staticmethod
    def get_action(key):
        # type = key.type ??
        symbol = key.sym
        mod = key.mod

        # Identify Action
        action = Action.from_key(symbol)

        # Movement
        movement = Movement.from_action(action)
        if movement is not None:
            return {'move': movement}

        # Non-movement
        match action:
            case Action.INVENTORY:
                return {'toggle': 'inventory'}
            case Action.INFO:
                return {'toggle': 'info_pane'}
            case Action.USE:
                return {'use': True}
            case Action.EXIT:
                return {'exit': True}
            case Action.FULLSCREEN:
                if KMOD_ALT:
                    return {'fullscreen': True}

        print(symbol)
        return {}

    @staticmethod
    def handle_mouse(mouse):
        return {}
