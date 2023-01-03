from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from definitions import Action, Movement, Event
from handlers.event import EventHandler
from .frame import Frame


def get_adj_center(center_pos, obj_pos):
    val = int(center_pos - (obj_pos // 2)) + 1
    if val < 0:
        return 0
    return val


class Title(Frame):
    menu_options: [str]
    selected: int
    text: [str]
    image: [str]

    def __init__(self, center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), size=(SCREEN_WIDTH, SCREEN_HEIGHT)):
        super(Title, self).__init__(center=center, size=size)
        self.menu_options = [
            'New Game',
            'Exit'
        ]
        self.selected = 0
        self.text = []
        self.image = []
        self.audio_source = 'resources/audio/bgm/title.wav'

        with open('resources/title_text.txt') as f:
            for line in f:
                self.text.append(line)

        with open('resources/title_image.txt') as f:
            for line in f:
                self.image.append(line)

    def handle_event(self, event: Event):
        # Move selection
        if Movement.is_move_action(event.action):
            dx, dy = event.params[0]
            index = self.selected
            if dy == -1:
                if index <= 0:
                    self.selected = len(self.menu_options) - 1
                else:
                    self.selected = index - 1

            elif dy == 1:
                if index >= len(self.menu_options) - 1:
                    self.selected = 0
                else:
                    self.selected = index + 1
            return

        # Others
        match event.action:
            case Action.USE:
                selected = self.menu_options[self.selected]
                match selected:
                    case 'Exit':
                        EventHandler.handle_event(Event(Action.EXIT))
                    case 'New Game':
                        EventHandler.window.new_game()

    def draw(self, con):
        # Draw border from top-left
        con.draw_frame(
            0,
            0,
            self.width,
            self.height,
            self.name,
            fg=(255, 255, 255),
            bg=(0, 0, 0),
            bg_blend=0
        )
        offset = self.draw_title(con)
        self.draw_menu_options(con, offset)

    def draw_title(self, con):
        center_x, center_y = self.center
        text_width = len(self.text[0])
        init_x = get_adj_center(center_x, text_width)
        init_y = 0
        offset = 0
        increment = 1

        for line in self.text:
            con.print(init_x, init_y + offset, line)
            offset += increment

        sword_height = len(self.image)
        sword_width = len(self.image[0])
        init_x = get_adj_center(center_x, sword_width)
        init_y = get_adj_center(center_y, sword_height)
        offset = 0
        for line in self.image:
            con.print(init_x, init_y + offset, line)
            offset += increment

        return offset

    def draw_menu_options(self, con, offset):
        center_x, center_y = self.center
        width = max([len(s) for s in self.menu_options])
        init_x = get_adj_center(center_x, width)
        init_y = offset
        increment = 1

        for idx, s in enumerate(self.menu_options):
            if self.selected == idx:
                con.print(init_x, init_y + offset, '>' + s)
            else:
                con.print(init_x, init_y + offset, ' ' + s)
            offset += increment
