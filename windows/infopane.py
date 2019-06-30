from windows.window import Frame
from windows.stats import Stats
from entities.entity import Entity
from constants import xy_to_idx
import tcod


class InfoPane(Frame):
    def __init__(self, init_pos=(0, 0), anchor=(0, 0), game_map=None):
        super(InfoPane, self).__init__(center=anchor, name='info_pane')
        self.entity = Entity((game_map.x, game_map.y), name='selector', symbol='*', color=tcod.yellow)
        self.count = 0
        self.game_map = game_map
        self.selection = game_map.player
        self.stats = Stats(self.selection, anchor)

    def select(self, move):
        if not move:
            return
        dx, dy = move

        dx = self.entity.x + dx
        dy = self.entity.y + dy

        if (self.game_map.top_left_x < dx < self.game_map.top_left_x + self.game_map.view_x) and \
           (self.game_map.top_left_y < dy < self.game_map.top_left_y + self.game_map.view_y):
            self.entity.move(move)
        self.selection = self.game_map.get_entity_from_abs(self.entity.pos)
        self.stats = Stats(self.selection, self.center)

    def draw(self, con):
        self.stats.draw(con)
        if self.count < 10:
            if self.selection:
                self.entity.symbol = self.selection.symbol
            else:
                self.entity.symbol = '-'
        else:
            self.entity.symbol = '*'
            if self.count > 20:
                self.count = 0

        self.entity.draw(con, self.entity.x, self.entity.y)
        self.count += 1
