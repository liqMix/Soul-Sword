from windows.inventory import *
from windows.game_map import *
from windows.infopane import *


def action_handler(action, window, player, map_window):
    move = action.get('move')
    toggle = action.get('toggle')
    use = action.get('use')
    if move:
        # Get top window
        top_frame = window.frames[window.frames_ordered[-1]]
        name = top_frame.name
        if name in ['inventory', 'info_pane', 'title']:
            # Manipulate window
            top_frame.select(move)

        elif name is 'gamemap':
            # Manipulate player's position on map
            game_map = top_frame.map
            if game_map.check_move(move, player):
                player.move(move)
                game_map.update_cell(player)
                game_map.get_items(player)
            game_map.enemy_turns()
            player.update_fov(game_map.tcod_map)
            return True

    if use:
        # Get top window
        top_frame = window.frames[window.frames_ordered[-1]]
        name = top_frame.name
        if name is 'title':
            selection = top_frame.selection
            if selection == 'New Game':
                window.remove_frame('title')
            elif selection is 'Exit':
                raise SystemExit()

    if toggle:
        # Toggle off
        if toggle in window.frames:
            if toggle is 'inventory':
                window.frames, window.frames_ordered = window.frames[toggle].history
            else:
                window.remove_frame(toggle)

        # Toggle on
        else:
            if toggle is 'inventory':
                inventory = Inventory(player, size=(SCREEN_WIDTH, SCREEN_HEIGHT))
                inventory.history = (window.frames, window.frames_ordered)
                inventory.select(None)

                window.remove_frames()
                window.add_frame(inventory)
                return True

            if toggle is 'info_pane':
                if 'inventory' not in window.frames:
                    init_pos = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
                    anchor = (SCREEN_WIDTH//4, 0)
                    info_pane = InfoPane(init_pos, anchor, map_window)
                    info_pane.history = (window.frames, window.frames_ordered)

                    window.add_frame(info_pane)
