class Controller:
    def __init__(self, messages):
        self.ticks = 0
        self.entities = []
        self.messages = messages

    def increment_ticks(self, n):
        self.ticks += n
