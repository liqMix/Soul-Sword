import tcod.map
import tcod.path
import tcod.random
from game_map.map import *
from entities.enemies import *
from windows.window import *


class MapWindow(Frame):
    def __init__(self, center=(0, 0), player=None):
        super(MapWindow, self).__init__(center=center, name='gamemap')

        num_rooms = random.randrange(ROOM['min_rooms'], ROOM['max_rooms'])
        self.map = GameMap(size_x=500, size_y=500, num_rooms=num_rooms, player=player)
        self.view_x = 80
        self.view_y = 24
        self.top_left_x = self.x - (self.view_x // 2)
        self.top_left_y = self.y - (self.view_y // 2)

    # Draw map to screen
    def draw(self, con):
        self.map.update_cells()
        player = self.map.player
        top_edge = self.top_left_y
        bot_edge = self.top_left_y + self.view_y
        left_edge = self.top_left_x
        right_edge = self.top_left_x + self.view_x

        half_width = self.view_x // 2
        half_height = self.view_y // 2

        # The cells to draw
        tile_x_range = range(player.x - half_width, player.x + half_width)
        tile_y_range = range(player.y - half_height, player.y + half_height)

        for y in tile_y_range:
            if 0 <= y < self.map.height:
                for x in tile_x_range:
                    if 0 <= x < self.map.width:
                        idx = xy_to_idx(x, y, self.map.width)
                        rel_x = x - player.x
                        rel_y = y - player.y
                        tile = self.map.tiles[idx]
                        item = tile['items']
                        entity = tile['entity']

                        if entity:
                            if entity.type is 'player':
                                entity.draw(con, self.x, self.y)
                            else:
                                entity.draw(con, rel_x + self.x, rel_y + self.y)

                        elif item:
                            item[0].draw(con, rel_x + self.x, rel_y + self.y)
                        else:
                            con.put_char(rel_x + self.x, rel_y + self.y, ord(' '), tcod.BKGND_NONE)

        # Draw border of map
        view_edge_symbol = ord('#')
        for x in range(self.view_x+1):
            con.put_char(x + left_edge, top_edge, view_edge_symbol, tcod.BKGND_NONE)
            con.put_char(x + left_edge, bot_edge, view_edge_symbol, tcod.BKGND_NONE)

        for y in range(self.view_y):
            con.put_char(left_edge, y + top_edge, view_edge_symbol, tcod.BKGND_NONE)
            con.put_char(right_edge, y + top_edge, view_edge_symbol, tcod.BKGND_NONE)

    def get_cell_from_abs(self, pos):
        x, y = pos
        rel_x = x - self.x + self.map.player.x
        rel_y = y - self.y + self.map.player.y
        idx = xy_to_idx(rel_x, rel_y, self.map.width)
        tile = self.map.tiles[idx]
        print(tile)
        return tile
