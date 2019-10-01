from windows.window import Frame

class Title(Frame):
    def __init__(self, anchor=(0, 0), size=(0,0)):
        x, y = anchor
        x = x // 5
        y = y // 5
        super(Title, self).__init__(center=(x,y), size=size, name='title')
        self.selections = ['New Game', 'Exit']
        self.selection = 'New Game'
        self.title_text = []
        self.title_sword = []
        with open('resources/title.txt') as f:
            for line in f:
                self.title_text.append(line)

        with open('resources/title_sword.txt') as f:
            for line in f:
                self.title_sword.append(line)




    def draw(self, con):
        con.draw_frame(0, 0, self.width, self.height,
                       fg=(255, 255, 255),
                       bg=(0, 0, 0),
                       bg_blend=0)
        offset = self.draw_title(con)
        self.draw_selections(con, offset)

    def select(self, move):
        dx, dy = move
        index = self.selections.index(self.selection)

        if dy == -1:
            if index <= 0:
                # play error sound
                return
            self.selection = self.selections[index-1]
            return

        if dy == 1:
            if index >= len(self.selections)-1:
                # play error sound
                return
            self.selection = self.selections[index+1]
            return

    def draw_title(self, con):
        init_x, init_y = self.center
        offset = 0
        increment = 1
        for line in self.title_text:
            con.print(init_x, init_y + offset, line)
            offset += increment

        init_x = init_x * 4
        offset += increment * 3
        for line in self.title_sword:
            con.print(init_x, init_y + offset, line)
            offset += increment

        return offset

    def draw_selections(self, con, offset):
        init_x, init_y = self.center
        init_x = int(init_x * 4.5)
        increment = 1
        init_y += increment * 5

        for s in self.selections:
            if self.selection is s:
                con.print(init_x, init_y + offset, '>' + s)
            else:
                con.print(init_x, init_y + offset, ' ' + s)
            offset += increment


