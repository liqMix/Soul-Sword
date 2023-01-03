import tcod


class Message:
    text: str
    color: tcod.Color

    def __init__(self, text, color=tcod.white):
        self.text = text
        self.color = color
