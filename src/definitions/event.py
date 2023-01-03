from typing import Any, List

from definitions import Action, Movement


class Event:
    action: Action
    params: List[Any]
    frame: Any

    def __init__(self, action, params=None, frame=None):
        if params is None:
            params = []

        self.action = action
        self.params = params
        self.frame = frame

    def is_move_event(self):
        return Movement.is_move_action(self.action)
