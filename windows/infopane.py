from windows.window import Frame
from entities.entity import Entity
import tcod


class InfoPane(Frame):
    def __init__(self, init_pos=(0, 0), anchor=(0, 0), game_map=None):
        super(InfoPane, self).__init__(center=anchor, name='info_pane')
        self.entity = Entity((game_map.x, game_map.y), name='selector', symbol='*', color=tcod.yellow)
        self.game_map = game_map
        self.selection = {'entity': game_map.map.player, 'items': []}

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
        if self.selection['entity']:
            self.entity.symbol = self.selection['entity'].symbol
        elif self.selection['items']:
            self.entity.symbol = self.selection['items'][-1].symbol
        else:
            self.entity.symbol = '*'

        self.entity.draw(con, self.entity.x, self.entity.y)

    def draw_infopane(self, con):
        if not self.selection:
            return

        entity = self.selection['entity']
        items = self.selection['items']
        offset = 2
        increment = 2
        top_anchor = self.y
        left_anchor = self.x - self.width

        if entity:
            # Draw name
            con.print(left_anchor, top_anchor + offset,
                      "Name: " + str(entity.name))
            offset += increment

            # Draw Level
            con.print(left_anchor, top_anchor + offset,
                      "Level:  " + str(entity.level))
            offset += increment

            # Draw HP
            con.print(left_anchor, top_anchor + offset,
                      "HP:  " + str(entity.current_hp) + ' / ' + str(entity.total_hp))
            offset += increment

            if entity.type is 'enemy':
                entity.picture.draw(con)
                '''
                con.print(left_anchor, top_anchor + offset,
                          "Data provided by JailBase.com")
                offset += increment
                con.print(left_anchor, top_anchor + offset,
                          "Individuals are innocent until proven guilty in a court of law.")
                offset += increment
                con.print(left_anchor, top_anchor + offset,
                          "Data is believed to be reliable but is provided \"as is\".")
                offset += increment
                con.print(left_anchor, top_anchor + offset,
                          "Contact the appropriate governmental agency to verify.")
                '''

        con.print(left_anchor, top_anchor + offset,
                  "Ground: ")
        offset += increment

        if items:
            for i in items:
                con.print(left_anchor+increment, top_anchor + offset,
                          str(i.name))
                offset += increment

                # Draw description
                con.print(left_anchor+(increment*2), top_anchor + offset,
                          str(i.desc))
                offset += increment
