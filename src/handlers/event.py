from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from windows.infopane import *
from windows.inventory import *


class EventHandler:

    @staticmethod
    def handle_action(action, window):
        player = window.controller.player
        if 'move' in action:
            EventHandler._handle_move(action['move'], player, window)
        elif 'toggle' in action:
            EventHandler._handle_toggle(action['toggle'], player, window)
        elif 'use' in action:
            EventHandler._handle_use(window)

    @staticmethod
    def _handle_move(move, player, window):
        move = move.value
        # Get top window
        top_frame = window.frames[window.frames_ordered[-1]]
        name = top_frame.name
        if name in ['inventory', 'info_pane', 'title']:
            # Manipulate window
            top_frame.select(move)

        elif name == 'gamemap':
            # Manipulate player's position on map
            game_map = top_frame.map
            if game_map.check_move(move, player):
                player.move(move)
                game_map.update_cell(player)
                game_map.get_items(player)
            game_map.enemy_turns()
            player.update_fov(game_map.tcod_map)
            return True

    @staticmethod
    def _handle_use(window):
        # Get top window
        top_frame = window.frames[window.frames_ordered[-1]]
        name = top_frame.name
        if name == 'title':
            selection = top_frame.selection
            if selection == 'New Game':
                window.remove_frame('title')
                window.new_game()
            elif selection == 'Exit':
                raise SystemExit()

    @staticmethod
    def _handle_toggle(toggle, player, window):
        # Toggle off
        if toggle in window.frames:
            if toggle == 'inventory':
                window.frames, window.frames_ordered = window.frames[toggle].history
            else:
                window.remove_frame(toggle)

        # Toggle on
        else:
            if toggle == 'inventory':
                inventory = Inventory(player, size=(SCREEN_WIDTH, SCREEN_HEIGHT))
                inventory.history = (window.frames, window.frames_ordered)
                inventory.select(None)

                window.remove_frames()
                window.add_frame(inventory)
                return True

            if toggle == 'info_pane':
                if 'gamemap' not in window.frames:
                    return False
                if 'inventory' not in window.frames:
                    init_pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                    anchor = (SCREEN_WIDTH // 4, 0)
                    info_pane = InfoPane(init_pos, anchor, window.frames['gamemap'])
                    info_pane.history = (window.frames, window.frames_ordered)

                    window.add_frame(info_pane)
