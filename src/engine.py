import tcod

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from definitions.window import Window
from frames import Title
from handlers.event import EventHandler
from handlers.input import InputHandler
from handlers.audio import AudioHandler


class Dispatch(tcod.event.EventDispatch):
    def ev_keydown(self, key):
        if not key:
            return
        event = InputHandler.get_input_event(key)
        EventHandler.handle_event(event)

    def ev_mousebuttondown(self, button):
        pass

    def ev_mousemotion(self, motion):
        pass


class Engine:
    tileset: tcod.tileset.Tileset
    dispatch: tcod.event.EventDispatch
    window: Window

    @staticmethod
    def init():
        # Set tileset
        Engine.tileset = tcod.tileset.load_tilesheet(
            'resources/tileset.png',
            columns=32,
            rows=8,
            charmap=tcod.tileset.CHARMAP_TCOD
        )

        # Init game window
        Engine.window = Window()
        EventHandler.window = Engine.window

        # Add title frame
        title = Title()
        Engine.window.push_frame(title)

        # Create event dispatch
        Engine.dispatch = Dispatch()

        # Start the game loop
        Engine.loop()

    @staticmethod
    def loop():
        with tcod.context.new(columns=SCREEN_WIDTH, rows=SCREEN_HEIGHT, tileset=Engine.tileset) as context:
            while True:
                con = context.new_console()
                con.clear()

                # Draw all frames in window
                for frame in Engine.window.frames:
                    frame.draw(con)

                context.present(con, integer_scaling=True)

                # Handle events
                for e in tcod.event.wait(timeout=1):
                    context.convert_event(e)
                    if isinstance(e, tcod.event.Quit):
                        AudioHandler.close()
                        raise SystemExit()
                    Engine.dispatch.dispatch(e)


if __name__ == '__main__':
    Engine.init()
