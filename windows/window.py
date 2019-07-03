class Window:
    def __init__(self, center=(0, 0), size=(0, 0)):
        self.center = center
        self.x, self.y = center
        self.width, self.height = size
        self.size = self.width * self.width
        self.frames = {}
        self.frames_ordered = []

    def add_frame(self, frame):
        self.frames[frame.name] = frame
        self.frames_ordered.append(frame.name)

    def remove_frame(self, name):
        del self.frames[name]
        self.frames_ordered.pop()

    def remove_frames(self):
        self.frames = {}
        self.frames_ordered = []


class Frame:
    def __init__(self, center=(0, 0), size=(0, 0), name='None'):
        self.center = center
        self.x, self.y = center
        self.width, self.height = size
        self.size = self.width * self.width
        self.name = name
        self.history = []
