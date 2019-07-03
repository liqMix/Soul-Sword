from windows.window import Frame
from windows.stats import Stats
from entities.entity import Entity
from constants import xy_to_idx
import tcod
import time
import threading


class InfoPane(Frame):
    def __init__(self, init_pos=(0, 0), anchor=(0, 0), game_map=None):
        super(InfoPane, self).__init__(center=anchor, name='info_pane')
        self.entity = Entity((game_map.x, game_map.y), name='selector', symbol='*', color=tcod.yellow)
        self.count = 0
        self.game_map = game_map
        self.selection = {'entity': game_map.player, 'items': []}

    def select(self, move):
        if not move:
            return
        dx, dy = move

        dx = self.entity.x + dx
        dy = self.entity.y + dy

        if (self.game_map.top_left_x < dx < self.game_map.top_left_x + self.game_map.view_x) and \
           (self.game_map.top_left_y < dy < self.game_map.top_left_y + self.game_map.view_y):
            self.entity.move(move)

        self.selection = self.game_map.get_cell_from_abs(self.entity.pos)

    def draw(self, con):
        self.draw_infopane(con)
        if self.count < 10:
            if self.selection['entity']:
                self.entity.symbol = self.selection['entity'].symbol
            elif self.selection['items']:
                self.entity.symbol = self.selection['items'][-1].symbol
        else:
            self.entity.symbol = '*'
            if self.count > 20:
                self.count = 0

        self.entity.draw(con, self.entity.x, self.entity.y)
        self.count += 1

    def draw_infopane(self, con):
        if not self.selection:
            return

        entity = self.selection['entity']
        items = self.selection['items']

        offset = 2
        increment = 2

        # Name
        # Desc

        count = 2
        #con.draw_frame(self.x, self.y, self.width, self.y + (offset*count), self.entity.name)
        top_anchor = self.y
        left_anchor = self.x - self.width

        con.print(left_anchor, top_anchor + offset,
                  "Entity:")
        offset += increment

        if entity:
            # Draw name
            con.print(left_anchor, top_anchor + offset,
                      "Name: " + str(entity.name))
            offset += increment

            # Draw description
            con.print(left_anchor, top_anchor + offset,
                      "Desc: " + str(entity.desc))
            offset += increment

            # Draw Level
            con.print(left_anchor, top_anchor + offset,
                      "Level:  " + str(entity.level))
            offset += increment

        con.print(left_anchor, top_anchor + offset,
                  "Ground: ")
        offset += increment

        if items:
            for i in items:
                con.print(left_anchor+increment, top_anchor + offset,
                          "Name: " + str(i.name))
                offset += increment

                # Draw description
                con.print(left_anchor+(increment*2), top_anchor + offset,
                          "Desc: " + str(i.desc))
                offset += increment
