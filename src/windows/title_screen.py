from windows.frame import Frame


def get_adj_center(center_pos, obj_pos):
    val = int(center_pos - (obj_pos//2)) + 1
    if val < 0:
        return 0
    return val


class Title(Frame):
    def __init__(self, center=(0, 0), size=(0, 0)):
        super(Title, self).__init__(center=center, size=size, name='title')
        self.selections = ['New Game', 'Exit']
        self.selection = 'New Game'
        self.title_text = []
        self.title_sword = []
        self.audio_source = 'resources/audio/title.wav'

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
        print(move)
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
        center_x, center_y = self.center
        text_width = len(self.title_text[0])
        init_x = get_adj_center(center_x, text_width)
        init_y = 0
        offset = 0
        increment = 1

        for line in self.title_text:
            con.print(init_x, init_y + offset, line)
            offset += increment

        sword_height = len(self.title_sword)
        sword_width = len(self.title_sword[0])
        init_x = get_adj_center(center_x, sword_width)
        init_y = get_adj_center(center_y, sword_height)
        offset = 0
        for line in self.title_sword:
            con.print(init_x, init_y + offset, line)
            offset += increment

        return offset

    def draw_selections(self, con, offset):
        center_x, center_y = self.center
        width = max([len(s) for s in self.selections])
        init_x = get_adj_center(center_x, width)
        init_y = offset
        increment = 1

        for s in self.selections:
            if self.selection is s:
                con.print(init_x, init_y + offset, '>' + s)
            else:
                con.print(init_x, init_y + offset, ' ' + s)
            offset += increment


