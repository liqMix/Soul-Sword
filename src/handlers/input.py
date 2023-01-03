from definitions.enums import Action, Movement
from definitions import Event
from tcod.event import KMOD_ALT


# Initializes the class
class InputHandler:

    @staticmethod
    def get_action(key) -> Action | None:
        # type = key.type ??
        symbol = key.sym

        # Identify Action
        action = Action.from_key(symbol)

        if not action:
            return

        # add mods to key->action listing
        if action == action.FULLSCREEN:
            if KMOD_ALT:
                return Action.FULLSCREEN
            return None

        return action

    @staticmethod
    def get_input_event(key):
        a = InputHandler.get_action(key)
        p = []
        if Movement.is_move_action(a):
            p = [Movement.from_action(a)]

        return Event(
            action=a,
            params=p
        )

    @staticmethod
    def handle_mouse(mouse):
        return {}
