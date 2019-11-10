from windows.frame import Frame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import math


class Loading(Frame):
    def __init__(self, center=(0, 0)):
        super(Loading, self).__init__(center,
                                      size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                                      name='loading')
        self.x = self.width // 4
        self.y = self.height // 2
        self.progress = 0
        self.status = ''

    def draw(self, con):
        con.draw_frame(self.x, self.y, self.width//2, self.height//12,
                       'Loading...',
                       fg=(255, 255, 255),
                       bg=(0, 0, 0),
                       bg_blend=0)

        self.draw_progress_bar(con)
        self.draw_status(con)

    def draw_progress_bar(self, con):
        progress = math.floor(self.progress * 50)
        progress = '#' * progress
        con.print(self.x + 2, self.y + 2, progress)

    def draw_status(self, con):
        con.print(self.x + 4, self.y + 4, self.status)

    def update(self, progress=None, status=None):
        if progress:
            self.progress = progress
        if status:
            self.status = status
