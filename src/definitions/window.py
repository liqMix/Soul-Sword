import threading

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from controller import Controller
from frames import Frame, Loading, Messages
from frames.map import Map
from frames.stats import Stats
from handlers.audio import AudioHandler


class Window:
    center: (int, int)
    x: int
    width: int
    height: int
    size: int
    frames: [Frame] = []

    def __init__(
            self,
            center=(
                    SCREEN_WIDTH // 2,
                    SCREEN_HEIGHT // 2),
            size=(
                    SCREEN_WIDTH - 5,
                    SCREEN_HEIGHT - 5)
    ):
        self.center = center
        self.x, self.y = center
        self.width, self.height = size
        self.size = self.width * self.width
        self.frames = []

    def get_top_frame(self) -> Frame | None:
        if len(self.frames) > 0:
            return self.frames[-1]
        return None

    def push_frame(self, frame: Frame):
        frame.window = self
        self.frames.append(frame)
        if frame.audio_source:
            AudioHandler.play_bgm(frame.audio_source)

    def pop_frame(self, frame=None) -> Frame | None:
        old_top = self.get_top_frame()
        removed = None
        if frame:
            for idx, f in enumerate(self.frames):
                if f == frame:
                    removed = f
                    self.frames = [*self.frames[:idx], *self.frames[idx + 1:]]
        else:
            removed = self.frames.pop()
        new_top = self.get_top_frame()
        if new_top and new_top != old_top and new_top.audio_source:
            AudioHandler.play_bgm(new_top.audio_source)
        return removed

    def clear_frames(self):
        self.frames = []

    def new_game(self):
        x = threading.Thread(target=self.init_game, args=())
        x.start()

    def init_game(self):
        loading_frame = Loading(self.center)
        Controller.loading = loading_frame
        self.pop_frame()
        self.push_frame(loading_frame)
        player = Controller.player
        game_map = Map(self.center, player=player)
        self.pop_frame(loading_frame)
        self.push_frame(Stats(player))
        self.push_frame(Messages())
        self.push_frame(game_map)
