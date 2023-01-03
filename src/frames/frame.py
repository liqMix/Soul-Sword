from __future__ import annotations

from typing import Any
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import tcod


class Frame:
    center: (int, int)
    x: int
    y: int
    width: int
    height: int
    size: int
    name: str
    window: Any
    audio_source: str | None = None

    def __init__(self, center=(0, 0), size=(SCREEN_WIDTH, SCREEN_HEIGHT), name=None, window=None):
        self.center = center
        self.x, self.y = center
        self.width, self.height = size
        self.size = self.width * self.height
        self.name = name
        self.window = window

    def handle_event(self, event):
        pass

    def draw(self, con: tcod.Console):
        # con.draw_rect(
        #     self.x,
        #     self.y,
        #     self.width,
        #     self.height,
        #     ch=0,
        #     fg=(255, 255, 255),
        #     bg=(0, 0, 0)
        # )
        con.draw_frame(
            self.x,
            self.y,
            self.width,
            self.height,
            self.name,
            fg=(255, 255, 255),
            bg=(0, 0, 0),
            bg_blend=0,
            clear=True
        )
