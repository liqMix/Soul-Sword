from windows.inventory import *
from windows.game_map import *
from windows.infopane import *

def action_handler(action, window, player, map):
    move = action.get('move')
    toggle = action.get('toggle')
    if move:
        # Get top window
        top_frame = window.frames[window.frames_ordered[-1]]
        name = top_frame.name
        if name in ['inventory', 'info_pane']:
            # Manipulate window
            top_frame.select(move)

        elif name is 'gamemap':
            # Manipulate player's position on map
            if top_frame.check_move(move, player):
                player.move(move)
                top_frame.get_items(player)
            return True

    if toggle:
        if toggle in window.frames:
            if toggle is 'inventory':
                window.frames, window.frames_ordered = window.frames[toggle].history
            else:
                window.remove_frame(toggle)
        else:
            # Add window
            if toggle is 'inventory':
                inventory = Inventory(player, size=(SCREEN_WIDTH, SCREEN_HEIGHT))
                inventory.history = (window.frames, window.frames_ordered)
                inventory.select(None)

                window.remove_frames()
                window.add_frame(inventory)
                return True

            if toggle is 'info_pane':
                init_pos = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
                anchor = (int(SCREEN_WIDTH/1.25), int(SCREEN_HEIGHT/1.25))
                info_pane = InfoPane(init_pos, anchor, map)
                info_pane.history = (window.frames, window.frames_ordered)

                #window.remove_frames()
                window.add_frame(info_pane)