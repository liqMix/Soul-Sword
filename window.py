class Window:
    def __init__(self, anchor=(0,0), size=(0, 0)):
        self.anchor = anchor
        self.x, self.y = anchor
        self.size = size
        self.width, self.height = size
        self.frames = {}
        self.frames_ordered = []

    def add_frame(self, frame):
        self.frames[frame.name] = frame
        self.frames_ordered.append(frame.name)

    def remove_frames(self):
        self.frames = {}
        self.frames_ordered = []


class Frame:
    def __init__(self, anchor=(0, 0), name='None'):
        self.anchor = anchor
        self.x, self.y = anchor
        self.name = name
        self.history = []
