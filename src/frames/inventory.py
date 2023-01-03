from definitions import Action
from .frame import Frame


# The inventory window listing all the player's items,
# their symbols, and their descriptions
class Inventory(Frame):
    selected: int = 0

    def __init__(self, entity, center=(0, 0)):
        super(Inventory, self).__init__(center, name='Inventory')
        self.entity = entity

    def draw(self, con):
        super(Inventory, self).draw(con)
        offset = 2
        increment = 2
        top_anchor = self.y
        left_anchor = self.x + 4
        if len(self.entity.inventory) > 0:
            if self.selected >= len(self.entity.inventory):
                self.selected = len(self.entity.inventory) - 1
            selected_item = self.entity.inventory[self.selected]
            for item in self.entity.inventory:
                if item == selected_item:
                    con.print(
                        left_anchor - 2,
                        top_anchor + offset,
                        '>'
                    )
                con.print(
                    left_anchor,
                    top_anchor + offset,
                    f'{item.name} ({item.symbol})',
                    fg=item.color
                )
                offset += increment
                con.print(
                    left_anchor + increment,
                    top_anchor + offset,
                    item.desc
                )
                offset += increment

    def handle_event(self, event):
        if event.is_move_event():
            move = event.params[0]
            x, y = move
            idx = self.selected
            # Move down in inventory
            if y == -1:
                if idx <= 0:
                    self.selected = len(self.entity.inventory) - 1
                else:
                    self.selected = idx - 1

            # Move up in inventory
            elif y == 1:
                if idx >= len(self.entity.inventory) - 1:
                    self.selected = 0
                else:
                    self.selected = idx + 1
        elif event.action == Action.INVENTORY:
            self.window.pop_frame()
