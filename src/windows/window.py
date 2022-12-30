import threading

from constants import *
from controller import Controller
from handlers import AudioHandler
from windows import Loading, MapWindow, Stats, Title


class Window:
    def __init__(self, center=(0, 0), size=(0, 0)):
        self.center = center
        self.x, self.y = center
        self.width, self.height = size
        self.size = self.width * self.width
        self.frames = {}
        self.frames_ordered = []
        self.controller = Controller()
        self.stats = None
        self.game_map = None

    def add_frame(self, frame):
        self.frames[frame.name] = frame
        self.frames_ordered.append(frame.name)
        if frame.audio_source:
            AudioHandler.play_bgm(frame.audio_source)

    def remove_frame(self, name):
        del self.frames[name]
        self.frames_ordered.pop()

    def remove_frames(self):
        self.frames = {}
        self.frames_ordered = []

    def show_title(self):
        self.add_frame(Title(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                             size=(SCREEN_WIDTH, SCREEN_HEIGHT)))

    def new_game(self):
        x = threading.Thread(target=self.init_game, args=())
        x.start()

    def init_game(self):
        self.controller.loading = Loading(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.add_frame(self.controller.loading)
        player = self.controller.player
        self.game_map = MapWindow(self.center, player=player)
        self.stats = Stats(player)
        self.remove_frame('loading')
        AudioHandler.stop_audio()
        self.add_frame(self.stats)
        self.add_frame(self.controller.messages)
        self.add_frame(self.game_map)
