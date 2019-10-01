from constants import *
import random as rand

class Controller:
    def __init__(self, messages):
        self.ticks = 0
        self.entities = []
        self.messages = messages

    def increment_ticks(self, n):
        self.ticks += n

    def attack(self, attacker, defender):
        if attacker.type is not defender.type:
            if defender.type is 'wall':
                pass
            else:
                self.messages.add_message(attacker.name + ' attacks ' + defender.name + ' with ' + attacker.weapon + '!')

                # Calculate miss chance #
                miss_chance = COMBAT['base_hit_chance'] + \
                              (attacker.stats['agi'] - (defender.stats['agi']) * COMBAT['hit_chance_per_diff'])
                if miss_chance < COMBAT['min_hit_chance']:
                    miss_chance = COMBAT['min_hit_chance']
                elif miss_chance > COMBAT['max_hit_chance']:
                    miss_chance = COMBAT['max_hit_chance']

                if rand.random() > miss_chance:
                    self.messages.add_message('But misses!')
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
