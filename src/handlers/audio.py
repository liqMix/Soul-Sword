import threading

import simpleaudio as sa


class AudioHandler:
    volume = 100
    muted = False
    _bgm_track: sa.PlayObject = None
    _sfx_tracks: [sa.PlayObject] = []

    @staticmethod
    def get_wave(source) -> sa.WaveObject:
        wave = sa.WaveObject.from_wave_file(source)
        return wave

    @staticmethod
    def loop_bgm(track: sa.PlayObject, wave: sa.WaveObject):
        t = track
        while AudioHandler._bgm_track == t:
            if not AudioHandler._bgm_track.is_playing():
                t = wave.play()
                AudioHandler._bgm_track = t

    @staticmethod
    def play_bgm(source):
        wave = AudioHandler.get_wave(source)
        if AudioHandler._bgm_track:
            AudioHandler._bgm_track.stop()
        track = wave.play()
        AudioHandler._bgm_track = track
        x = threading.Thread(target=AudioHandler.loop_bgm, args=(track, wave,))
        x.start()

    @staticmethod
    def play_sfx(source):
        wave = AudioHandler.get_wave(source)
        track = wave.play()
        AudioHandler._sfx_tracks.append(track)

    @staticmethod
    def stop_audio():
        AudioHandler._bgm_track.stop()
        for t in AudioHandler._sfx_tracks:
            t.stop()

    @staticmethod
    def clear_audio():
        AudioHandler.stop_audio()
        AudioHandler._bgm_track = None
        AudioHandler._sfx_tracks = []
