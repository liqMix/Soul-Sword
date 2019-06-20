from window import *
class Stats(Window):
    def __init__(self, entity, anchor=(1, 1)):
        super(Stats, self).__init__(anchor)
        self.width, self.height = (20, 30)
        self.entity = entity

    def draw(self, con):
        # Name
        # Life
        # Position
        # Weapon
        # --------- 4 Offset
        count = 5
        # Inventory
        #   ...
        #   ...
        for item in self.entity.inventory:
            count += 1


        offset = 2
        increment = 2

        con.draw_frame(self.x, self.y, self.width, self.y + (offset*count), "Player Stats")
        top_anchor = self.y
        left_anchor = self.x + 2

        # Draw life points
        con.print(left_anchor, top_anchor + offset,
                    "Life: " + str(self.entity.hp))
        offset += increment

        # Draw position
        con.print(left_anchor, top_anchor + offset,
                    "X,Y: " + str(self.entity.pos))
        offset += increment

        # Draw Current Weapon
        con.print(left_anchor, top_anchor + offset,
                    "Weapon: " + str(self.entity.weapon))
        offset += increment

        # Draw Inventory
        con.print(left_anchor, top_anchor + offset,
                  "Inventory: ")
        offset += increment

        if self.entity.inventory is not []:
            for item in self.entity.inventory:
                con.print(left_anchor+2, top_anchor + offset,
                          item.name)
                offset += increment
