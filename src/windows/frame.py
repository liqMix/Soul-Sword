class Frame:
    def __init__(self, center=(0, 0), size=(0, 0), name='None'):
        self.center = center
        self.x, self.y = center
        self.width, self.height = size
        self.size = self.width * self.height
        self.name = name
        self.audio_source = None
        self.history = []
