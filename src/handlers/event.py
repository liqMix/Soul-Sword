from typing import Any

from handlers.audio import AudioHandler
from definitions import Action
import tcod


class EventHandler:
    window: Any

    @staticmethod
    def handle_event(event):
        match event.action:
            # Handle system
            case Action.EXIT:
                AudioHandler.close()
                raise SystemExit()
            case Action.FULLSCREEN:
                tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
            case _:
                # Get top window and let it handle event
                top = EventHandler.window.get_top_frame()
                top.handle_event(event)
