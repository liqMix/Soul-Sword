from inventory import *
from game_map import *


def action_handler(action, window, player):
    move = action.get('move')
    toggle = action.get('toggle')
    if move:
        # Get top window
        top_frame = window.frames[window.frames_ordered[-1]]
        name = top_frame.name
        print(name)
        if name is 'inventory':
            # Manipulate inventory window
            pass

        elif name is 'gamemap':
            # Manipulate player's position on map
            if top_frame.check_move(move, player):
                player.move(move)
                top_frame.get_items(player)
                print(str(player.pos))
            return True

    if toggle:
        print(toggle)
        if toggle in window.frames:
            window.frames, window.frames_ordered = window.frames[toggle].history

        else:
            # Add window
            if toggle is 'inventory':
                inventory = Inventory(player, size=(SCREEN_WIDTH, SCREEN_HEIGHT))
                inventory.history = (window.frames, window.frames_ordered)

                window.remove_frames()
                window.add_frame(inventory)