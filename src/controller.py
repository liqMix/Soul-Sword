import random as rand

from entities.player import *
from handlers import AudioHandler
from windows.messages import Messages


class Controller:
    def __init__(self):
        self.ticks = 0
        self.entities = []
        self.messages = Messages()
        self.player = Player(controller=self)
        self.loading = None

    def increment_ticks(self, n):
        self.ticks += n

    def attack(self, attacker, defender):
        if attacker.type is not defender.type:
            if defender.type is 'wall':
                pass
            else:
                self.messages.add_message(
                    attacker.name + ' attacks ' + defender.name + ' with ' + attacker.weapon + '!')

                # Calculate miss chance #
                miss_chance = COMBAT['base_hit_chance'] + \
                              (attacker.stats['agi'] - (defender.stats['agi']) * COMBAT['hit_chance_per_diff'])
                if miss_chance < COMBAT['min_hit_chance']:
                    miss_chance = COMBAT['min_hit_chance']
                elif miss_chance > COMBAT['max_hit_chance']:
                    miss_chance = COMBAT['max_hit_chance']

                if rand.random() > miss_chance:
                    self.messages.add_message('But misses!')
                    AudioHandler.play_sfx('resources/audio/miss.wav')
                else:
                    damage = attacker.stats['str'] - defender.stats['def']
                    if damage < 0:
                        damage = 0
                    if defender.type is "player":
                        color = tcod.red
                    else:
                        color = tcod.white
                    self.messages.add_message(defender.name + ' suffers ' + str(damage) + ' points of damage!', color)
                    defender.current_hp -= damage
                    AudioHandler.play_sfx('resources/audio/' + attacker.weapon + '.wav')
                    if defender.current_hp <= 0:
                        self.messages.add_message(defender.name + ' perishes!', color)
                        AudioHandler.play_sfx('resources/audio/ded.wav')
