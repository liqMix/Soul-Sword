from window import *


# The inventory window listing all the player's items,
# their symbols, and their descriptions
class Inventory(Frame):
    def __init__(self, entity, anchor=(0, 0), size=(0, 0)):
        super(Inventory, self).__init__(anchor, name='inventory')
        self.width, self.height = size
        self.entity = entity
        self.selection = None

    def draw(self, con):
        offset = 2
        increment = 2

        con.draw_frame(self.x, self.y, self.width, self.height, "Inventory",
                       fg=(255, 255, 255),
                       bg=(0, 0, 0),
                       bg_blend=0)
        top_anchor = self.y
        left_anchor = self.x + 4
        if self.entity.inventory is not []:
            for item in self.entity.inventory:
                if item == self.selection:
                    con.print(left_anchor-2, top_anchor + offset,
                              ">")
                con.print(left_anchor, top_anchor + offset,
                          item.name + "  (" + item.symbol + ")")
                offset += increment
                con.print(left_anchor+increment, top_anchor + offset,
                          item.desc)
                offset += increment

    def select(self, move):
        if move is None:
            if not self.entity.inventory:
                print("Here")
                return
            self.selection = self.entity.inventory[0]
            print(self.selection)
            return

        x, y = move
        index = self.entity.inventory.index(self.selection)

        # Move down in inventory
        if y == -1:
            if index <= 0:
                # play error sound
                return
            self.selection = self.entity.inventory[index-1]
            return

        # Move up in inventory
        if y == 1:
            if index >= len(self.entity.inventory)-1:
                # play error sound
                return
            self.selection = self.entity.inventory[index+1]
            return
