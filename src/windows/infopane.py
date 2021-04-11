from windows.frame import Frame
from entities.entity import Entity
import tcod
from utility.conversion import xy_to_idx


class InfoPane(Frame):
    def __init__(self, init_pos=(0, 0), anchor=(0, 0), game_map=None):
        super(InfoPane, self).__init__(center=anchor, name='info_pane')
        self.entity = Entity((game_map.map.player.x, game_map.map.player.y), name='selector', symbol='*', color=tcod.yellow)
        self.game_map = game_map
        self.selection = {'entity': game_map.map.player, 'items': []}

    def select(self, move):
        if not move:
            return

        game_map = self.game_map
        dx, dy = move
        dx = self.entity.x + dx
        dy = self.entity.y + dy

        if not self.game_map.map.player.view[dy, dx]:
            return

        self.entity.move(move)
        print(self.entity.pos)
        self.selection = game_map.map.tiles[xy_to_idx(self.entity.x, self.entity.y, game_map.map.width)]

    def draw(self, con):
        self.draw_infopane(con)
        if self.selection['entity']:
            self.entity.symbol = self.selection['entity'].symbol
        elif self.selection['items']:
            self.entity.symbol = self.selection['items'][-1].symbol
        else:
            self.entity.symbol = '*'

        self.entity.draw(con,
                         self.entity.x - self.game_map.map.player.x + self.game_map.x,
                         self.entity.y - self.game_map.map.player.y + self.game_map.y)

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
                      "Name: " + str(entity.name), fg=entity.color)
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
                con.print(left_anchor, top_anchor + offset, "Charges:  ")
                offset += increment
                for c in entity.charges[:5]:
                    con.print(left_anchor + increment, top_anchor + offset, c)
                    offset += increment
                if len(entity.charges) > 5:
                    con.print(left_anchor + increment, top_anchor + offset, '...')
                    offset += increment
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
                # Draw item name
                con.print(left_anchor+increment, top_anchor + offset,
                          str(i.name), fg=i.color)
                offset += increment

                # Draw item description
                con.print(left_anchor+(increment*2), top_anchor + offset,
                          str(i.desc))
                offset += increment
