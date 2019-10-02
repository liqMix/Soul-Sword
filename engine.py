import tcod.event
from entities.player import *
from windows.game_map import *
from windows.stats import *
from windows.messages import *
from windows.title_screen import *
from handlers.input_handlers import handle_keys
from handlers.event_handlers import action_handler
from controller import Controller


def main():
    class State(tcod.event.EventDispatch):
        def ev_quit(self, event):
            raise SystemExit()

        def ev_keydown(self, event):
            action = handle_keys(event)
            exit = action.get('exit')
            fullscreen = action.get('fullscreen')

            if exit:
                self.ev_quit(event)

            if fullscreen:
                tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

            action_handler(action, window, player, game_map, controller)

        def ev_mousebuttondown(self, event):
            pass

        def ev_mousemotion(self, event):
            pass

    # Init game window
    center = (SCREEN_WIDTH // 2,
              SCREEN_HEIGHT // 2)
    window = Window(size=(SCREEN_WIDTH-5, SCREEN_HEIGHT-5))

    messages = Messages()
    controller = Controller(messages)
    player = Player(controller=controller)
    game_map = MapWindow(center, player=player)
    stats = Stats(player)

    window.add_frame(stats)
    window.add_frame(messages)
    window.add_frame(game_map)
    window.add_frame(Title(center, size=(SCREEN_WIDTH, SCREEN_HEIGHT)))
    controller.play_audio(window.frames['title'].audio_source, loop=True)
    # Initializes console
    tcod.console_set_custom_font('resources/tileset.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    con_root = tcod.console_init_root(w=SCREEN_WIDTH, h=SCREEN_HEIGHT,
                                 title='Soul Sword',
                                 vsync=False,
                                 renderer=tcod.RENDERER_SDL2)
    con = tcod.console.Console(SCREEN_WIDTH, SCREEN_HEIGHT)
    state = State()

    # Game loop
    while True:
        con.clear()

        # Draw all frames
        for frame in window.frames_ordered:
            window.frames[frame].draw(con)

        tcod.console_flush()
        con.blit(con_root)

        # Handle events
        for event in tcod.event.wait():
            state.dispatch(event)


if __name__ == '__main__':
    main()
