from src.windows.messages import Messages
from src.entities.player import *
import random as rand
import simpleaudio as sa
import threading


class Controller:
    def __init__(self):
        self.ticks = 0
        self.entities = []
        self.messages = Messages()
        self.audio_tracks = []
        self.player = Player(controller=self)
        self.loading = None

    def play_audio(self, source, loop=False):
        wave_object = sa.WaveObject.from_wave_file(source)

        audio_track = wave_object.play()
        self.audio_tracks.append(audio_track)

        if loop:
            x = threading.Thread(target=self.loop_audio, args=(audio_track, wave_object,))
            x.start()

    def loop_audio(self, track, wave_object):
        while track in self.audio_tracks:
            track.wait_done()
            if track not in self.audio_tracks:
                return
            self.audio_tracks.remove(track)
            self.audio_tracks.append(wave_object.play())

    def clear_audio(self):
        for track in self.audio_tracks:
            if not track.is_playing():
                self.audio_tracks.remove(track)

    def stop_audio(self):
        for track in self.audio_tracks:
            track.stop()
        self.audio_tracks = []

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
                    self.play_audio('resources/audio/miss.wav')
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
                    self.play_audio('resources/audio/' + attacker.weapon + '.wav')
                    if defender.current_hp <= 0:
                        self.messages.add_message(defender.name + ' perishes!', color)
                        self.play_audio('resources/audio/ded.wav')
