import tcod

from definitions.message import Message


class MessageHandler:
    messages: [Message] = []

    @staticmethod
    def create_message(text: str, color: tcod.Color = None):
        m = Message(text, color)
        MessageHandler.add_message(m)

    @staticmethod
    def add_message(m: Message):
        MessageHandler.messages.append(m)
