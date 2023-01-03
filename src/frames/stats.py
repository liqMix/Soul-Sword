from controller import Controller
from .frame import Frame


# Stats window containing player details
class Stats(Frame):
    def __init__(self, entity, anchor=(1, 1)):
        super(Stats, self).__init__(anchor, name='stats')
        self.width, self.height = (20, 30)
        self.entity = entity

    def draw(self, con):
        if not self.entity:
            return
        offset = 2
        increment = 2

        if self.entity.type == 'player':
            # Ticks
            # Name
            # Life
            # Position
            # Weapon
            # --------- 5 Offset
            count = 6
            # Inventory
            #   ...
            #   ...
            # for item in self.entity.inventory:
            #    count += 1

            con.draw_frame(self.x, self.y, self.width, self.y + (offset * count), self.entity.name)
            top_anchor = self.y
            left_anchor = self.x + 2
            # Draw level
            con.print(left_anchor, top_anchor + offset,
                      "Level: " + str(self.entity.level))
            offset += increment
            # Draw ticks
            con.print(left_anchor, top_anchor + offset,
                      "Ticks: " + str(Controller.tick))
            offset += increment

            # Draw life points
            con.print(left_anchor, top_anchor + offset,
                      "Life: " + str(self.entity.current_hp) + " / " + str(self.entity.total_hp))
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
            '''
            con.print(left_anchor, top_anchor + offset,
                      "Inventory: ")
            offset += increment

            if self.entity.inventory is not []:
                for item in self.entity.inventory:
                    con.print(left_anchor+2, top_anchor + offset,
                              item.name)
                    offset += increment
            '''
