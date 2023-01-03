from __future__ import annotations
from enum import Enum
from .actions import Action as Action


class Movement(Enum):
    N = (0, -1)
    S = (0, 1)
    W = (-1, 0)
    E = (1, 0)

    NW = (-1, -1)
    NE = (1, -1)
    SW = (-1, 1)
    SE = (1, 1)

    WAIT = (0, 0)

    @staticmethod
    def is_move_action(action: Action):
        return action in action_to_move

    @staticmethod
    def from_action(action: Action) -> Movement | None:
        if action in action_to_move:
            return action_to_move[action].value
        return None


action_to_move = {
    Action.N: Movement.N,
    Action.S: Movement.S,
    Action.E: Movement.E,
    Action.W: Movement.W,

    Action.NE: Movement.NE,
    Action.NW: Movement.NW,
    Action.SE: Movement.SE,
    Action.SW: Movement.SW,

    Action.WAIT: Movement.WAIT
}