import tcod.event
from player import *
from game_map import *
from stats import *
from input_handlers import handle_keys, handle_mouse
from event_handlers import action_handler
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

            action_handler(action, window, player)

        def ev_mousebuttondown(self, event):
            pass

        def ev_mousemotion(self, event):
            pass

    center = (SCREEN_WIDTH // 2,
              SCREEN_HEIGHT // 2)
    window = Window(size=(SCREEN_WIDTH-5, SCREEN_HEIGHT-5))
    controller = Controller()
    player = Player(center, controller)
    game_map = GameMap(center, entities=[player])
    stats = Stats(player)
    window.add_frame(stats)
    window.add_frame(game_map)
    tcod.console_set_custom_font('tileset.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    con_root = tcod.console_init_root(w=SCREEN_WIDTH, h=SCREEN_HEIGHT,
                                 title='CorpseSword',
                                 vsync=True,
                                 renderer=tcod.RENDERER_SDL2)
    con = tcod.console.Console(SCREEN_WIDTH, SCREEN_HEIGHT)
    state = State()

    while True:
        con.clear()

        # Draw frames starting with the top of list
        for frame in window.frames_ordered[::-1]:
            window.frames[frame].draw(con)

        tcod.console_flush()
        con.blit(con_root)

        for event in tcod.event.wait():
            state.dispatch(event)


if __name__ == '__main__':
    main()
