import tcod.event

from constants import *
from handlers import AudioHandler, EventHandler, InputHandler
from windows.window import Window


def main():
    class State(tcod.event.EventDispatch):
        def ev_quit(self, event):
            AudioHandler.stop_audio()
            raise SystemExit()

        def ev_keydown(self, event):
            if not event:
                return
            action = InputHandler.get_action(event)
            if 'exit' in action:
                self.ev_quit(event)

            if 'fullscreen' in action:
                tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

            EventHandler.handle_action(action, window)

        def ev_mousebuttondown(self, event):
            pass

        def ev_mousemotion(self, event):
            pass

    # Initializes console
    tileset = tcod.tileset.load_tilesheet('resources/tileset.png', columns=32, rows=8,
                                          charmap=tcod.tileset.CHARMAP_TCOD)
    state = State()

    # Init game window
    center = (SCREEN_WIDTH // 2,
              SCREEN_HEIGHT // 2)
    window = Window(center=center, size=(SCREEN_WIDTH - 5, SCREEN_HEIGHT - 5))
    window.show_title()

    # Game loop
    with tcod.context.new(columns=SCREEN_WIDTH, rows=SCREEN_HEIGHT, tileset=tileset) as context:
        while True:
            con = context.new_console()
            con.clear()

            # Draw all frames
            for frame in window.frames_ordered:
                window.frames[frame].draw(con)

            context.present(con, integer_scaling=True)

            # Handle events
            for event in tcod.event.wait(timeout=1):
                context.convert_event(event)
                state.dispatch(event)


if __name__ == '__main__':
    main()
