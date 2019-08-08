class Controller:
    def __init__(self):
        self.ticks = 0
        self.entities = []

    def increment_ticks(self, n):
        self.ticks += n
