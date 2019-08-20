from windows.window import Frame
from constants import *


# Manages output to the user of events
class Messages(Frame):
    def __init__(self):
        super(Messages, self).__init__(center=(int(SCREEN_WIDTH//9),
                                               int(SCREEN_HEIGHT - SCREEN_HEIGHT//3.25)),
                                       size=(MESSAGES['width'], MESSAGES['height']),
                                       name='Messages')
        self.lines = []

    def draw(self, con):
        con.draw_frame(self.x, self.y, self.width, self.height)

        if self.lines:
            bottom = self.y+self.height
            offset = 2
            increment = 2

            for line in reversed(self.lines[-MESSAGES['max_lines']:]):
                con.print(self.x + increment, bottom - offset, line)
                offset += increment

    # Splits the string based on the width of the message box
    def add_message(self, string):
        max_len = MESSAGES['width'] - 4
        if len(string) <= max_len:
            self.lines.append(string)
            return

        while string > max_len:
            self.lines.append(string[:max_len])
            string = string[max_len:]
        self.lines.append(string)
