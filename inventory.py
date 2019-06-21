from window import *


# The inventory window listing all the player's items,
# their symbols, and their descriptions
class Inventory(Frame):
    def __init__(self, entity, anchor=(0, 0), size=(0, 0)):
        super(Inventory, self).__init__(anchor, name='inventory')
        self.width, self.height = size
        self.entity = entity

    def draw(self, con):
        offset = 2
        increment = 2

        con.draw_frame(self.x, self.y, self.width, self.height, "Inventory",
                       fg=(255, 255, 255),
                       bg=(0, 0, 0),
                       bg_blend=0)
        top_anchor = self.y
        left_anchor = self.x + 2

        if self.entity.inventory is not []:
            for item in self.entity.inventory:
                con.print(left_anchor, top_anchor + offset,
                          item.name + "(" + item.symbol + ")")
                offset += increment
                con.print(left_anchor+increment, top_anchor + offset,
                          item.desc)
                offset += increment
