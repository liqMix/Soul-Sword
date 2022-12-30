from __future__ import annotations
from enum import Enum

import tcod.event_constants as keys


class Action(Enum):
    # Movement Actions
    N = 'n'
    S = 's'
    W = 'w'
    E = 'e'
    NW = 'nw'
    NE = 'ne'
    SW = 'sw'
    SE = 'se'
    WAIT = 'wait'

    # Player Actions
    USE = 'use'

    # UI Actions
    INVENTORY = 'inventory'
    INFO = 'info'

    # System Actions
    FULLSCREEN = 'fullscreen'
    EXIT = 'exit'

    @staticmethod
    def from_key(symbol: int) -> Action:
        for action, symbols in action_to_key.items():
            if symbol in symbols:
                return action


action_to_key = {
    Action.N: [keys.K_w, keys.K_UP, keys.K_KP_8],
    Action.S: [keys.K_s, keys.K_DOWN, keys.K_KP_2],
    Action.E: [keys.K_d, keys.K_RIGHT, keys.K_KP_6],
    Action.W: [keys.K_a, keys.K_LEFT, keys.K_KP_4],
    Action.NE: [keys.K_e, keys.K_KP_9],
    Action.NW: [keys.K_q, keys.K_KP_7],
    Action.SE: [keys.K_c, keys.K_KP_3],
    Action.SW: [keys.K_z, keys.K_KP_1],
    Action.WAIT: [keys.K_SPACE],

    Action.USE: [keys.K_KP_5, keys.SCANCODE_KP_ENTER, 13],

    Action.INVENTORY: [keys.K_i],
    Action.INFO: [keys.K_f],

    Action.EXIT: [keys.K_ESCAPE],
    Action.FULLSCREEN: [keys.K_RETURN]
}
