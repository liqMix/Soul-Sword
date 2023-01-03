import random as rand

from entities.player import *
from frames.loading import Loading
from handlers.audio import AudioHandler
from handlers.message import MessageHandler


class Controller:
    tick = 0
    entities = []
    player: Player = Player()
    loading: Loading = None

    @staticmethod
    def increment_ticks(n: int = 1):
        Controller.tick += n

    @staticmethod
    def attack(attacker, defender):
        if attacker.type is not defender.type:
            if defender.type == 'wall':
                pass
            else:
                MessageHandler.create_message(
                    attacker.name + ' attacks ' + defender.name + ' withsssssa ' + attacker.weapon + '!'
                )

                # Calculate miss chance #
                miss_chance = COMBAT['base_hit_chance'] + \
                              (
                                      attacker.stats['agi'] - (defender.stats['agi']) * COMBAT['hit_chance_per_diff'])
                if miss_chance < COMBAT['min_hit_chance']:
                    miss_chance = COMBAT['min_hit_chance']
                elif miss_chance > COMBAT['max_hit_chance']:
                    miss_chance = COMBAT['max_hit_chance']

                if rand.random() > miss_chance:
                    MessageHandler.create_message('But misses!')
                    AudioHandler.play_sfx('resources/audio/sfx/miss.wav')
                else:
                    damage = attacker.stats['str'] - defender.stats['def']
                    if damage < 0:
                        damage = 0
                    if defender.type == "player":
                        color = tcod.red
                    else:
                        color = tcod.white
                    MessageHandler.create_message(defender.name + ' suffers ' + str(damage) + ' points of damage!',
                                                  color)
                    defender.current_hp -= damage
                    AudioHandler.play_sfx('resources/audio/sfx/' + attacker.weapon + '.wav')
                    if defender.current_hp <= 0:
                        MessageHandler.create_message(defender.name + ' perishes!', color)
                        AudioHandler.play_sfx('resources/audio/sfx/ded.wav')
