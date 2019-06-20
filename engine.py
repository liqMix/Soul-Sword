import tcod as tcod
import tcod.event
from player import *
from map import *
from stats import *
from input_handlers import handle_keys, handle_mouse


def main():
    class State(tcod.event.EventDispatch):
        def ev_quit(self, event):
            raise SystemExit()

        def ev_keydown(self, event):
            print(event)
            action = handle_keys(event)
            exit = action.get('exit')
            fullscreen = action.get('fullscreen')
            move = action.get('move')

            if move:
                if map.check_move(move, player):
                    player.move(move)
                    player.add_items(map.get_items(player.pos))
                    print(str(player.pos))

            if exit:
                self.ev_quit(self, event)

            if fullscreen:
                tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

        def ev_mousebuttondown(self, event):
            pass

        def ev_mousemotion(self, event):
            pass

    screen_width = 80
    screen_height = 50
    center = (screen_width // 2,
              screen_height // 2)

    player = Player(center)
    map = Map(center)

    stats = Stats(player)
    tcod.console_set_custom_font('tileset.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(screen_width, screen_height, 'tcod Test', False)
    con = tcod.console_new(screen_width, screen_height)
    tcod.console_set_default_foreground(con, tcod.white)

    state = State()
    while True:
        tcod.console_put_char(con, player.pos_x, player.pos_y, '@', tcod.BKGND_NONE)
        tcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        tcod.console_flush()
        tcod.console_put_char(con, player.pos_x, player.pos_y, ' ', tcod.BKGND_NONE)
        map.draw(con)
        stats.draw(con)
        for event in tcod.event.wait():
            state.dispatch(event)



'''
    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)

        tcod.console_set_default_foreground(con, tcod.white)
        tcod.console_put_char(con, player_x, player_y, '@', tcod.BKGND_NONE)
        tcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        tcod.console_flush()

        tcod.console_put_char(con, player_x, player_y, ' ', tcod.BKGND_NONE)

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player_x += dx * PLAYER_SPEED
            player_y += dy * PLAYER_SPEED

            print(str(player_x) + " " + str(player_y))

            # Enforce screen bounds
            if player_x <= 0:
                player_x = 0
            elif player_x >= screen_width:
                player_x = screen_width-1

            if player_y <= 0:
                player_y = 0
            elif player_y >= screen_height:
                player_y = screen_height-1

        if exit:
            return True

        if fullscreen:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
'''


if __name__ == '__main__':
    main()
