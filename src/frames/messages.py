import re

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MESSAGE_CONFIG
from definitions.message import Message
from handlers.message import MessageHandler
from .frame import Frame


# Manages output to the user of events
class Messages(Frame):
    MAX_LINES = MESSAGE_CONFIG['max_lines']

    def __init__(self):
        width = int(SCREEN_WIDTH // 1.25)
        height = int(SCREEN_HEIGHT // 4)
        super(Messages, self).__init__(
            center=(
                int(SCREEN_WIDTH // 9),
                int(SCREEN_HEIGHT - SCREEN_HEIGHT // 3.25)
            ),
            size=(width, height),
            name='Messages'
        )

    # Draws the message box and the messages
    def draw(self, con):
        con.draw_frame(self.x, self.y, self.width, self.height)
        messages = MessageHandler.messages
        if len(messages) > 0:
            bottom = self.y + self.height
            offset = 2
            increment = 2
            split_messages = [self.split_message(m) for m in messages]
            message_list = []
            for m in split_messages:
                message_list = [*message_list, *m]
            for m in reversed(message_list[-self.MAX_LINES:]):
                con.print(self.x + increment, bottom - offset, m.text, fg=m.color)
                offset += increment

    # Splits the message into set of messages based on the width of the message box
    def split_message(self, message) -> [Message]:
        max_len = self.width - 4
        if len(message.text) <= max_len:
            return [message]

        messages = []
        lines = re.findall('.' * max_len, message.text)
        for l in lines:
            messages.append(
                Message(l, message.color)
            )
        return messages
