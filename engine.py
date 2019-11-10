import tcod.event
from constants import *
from windows.window import Window
from handlers.input_handlers import handle_keys
from handlers.event_handlers import action_handler


def main():
    class State(tcod.event.EventDispatch):
        def ev_quit(self, event):
            if window.controller:
                window.controller.stop_audio()
            raise SystemExit()

        def ev_keydown(self, event):
            if not event:
                return
            action = handle_keys(event)
            exit = action.get('exit')
            fullscreen = action.get('fullscreen')

            if exit:
                self.ev_quit(event)

            if fullscreen:
                tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

            action_handler(action, window)

        def ev_mousebuttondown(self, event):
            pass

        def ev_mousemotion(self, event):
            pass

    # Initializes console
    tcod.console_set_custom_font('resources/tileset.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    con_root = tcod.console_init_root(w=SCREEN_WIDTH, h=SCREEN_HEIGHT,
                                      title='Soul Sword',
                                      vsync=False,
                                      renderer=tcod.RENDERER_SDL2)

    con = tcod.console.Console(SCREEN_WIDTH, SCREEN_HEIGHT)
    state = State()

    # Init game window
    center = (SCREEN_WIDTH // 2,
              SCREEN_HEIGHT // 2)
    window = Window(center=center, size=(SCREEN_WIDTH-5, SCREEN_HEIGHT-5))
    window.show_title()

    # Game loop
    while True:
        con.clear()

        # Draw all frames
        for frame in window.frames_ordered:
            window.frames[frame].draw(con)

        tcod.console_flush()
        con.blit(con_root)

        # Handle events
        for event in tcod.event.wait(timeout=1):
            state.dispatch(event)


if __name__ == '__main__':
    main()
