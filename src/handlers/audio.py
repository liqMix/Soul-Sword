import threading
import time
import wave

import pyaudio

CHUNK = 1024


class AudioHandler:
    volume = 100
    muted = False
    _closed = False
    _p = pyaudio.PyAudio()
    _bgm_stream: pyaudio.Stream = None
    _bgm_source: str = ''
    _sfx_streams: [pyaudio.Stream] = []
    _threads = []

    @staticmethod
    def get_stream(source) -> pyaudio.Stream:
        def cb(in_data, frame_count, time_info, status):
            data = wf.readframes(frame_count)
            return data, pyaudio.paContinue

        wf = wave.open(source, 'rb')
        p = AudioHandler._p
        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True,
            stream_callback=cb
        )
        return stream

    @staticmethod
    def play_stream(stream: pyaudio.Stream):
        try:
            while stream.is_active() and not AudioHandler._closed:
                time.sleep(0.1)
            stream.close()
        except OSError:
            return

    @staticmethod
    def _loop_bgm(source: str):
        while AudioHandler._bgm_source == source and AudioHandler._closed:
            if not AudioHandler._bgm_stream.is_active():
                AudioHandler.play_bgm(source)
                return

    @staticmethod
    def play_bgm(source):
        # If already playing requested source
        if source == AudioHandler._bgm_source and AudioHandler._bgm_stream.is_active():
            return
        AudioHandler._bgm_source = source
        stream = AudioHandler.get_stream(source)
        if AudioHandler._bgm_stream:
            AudioHandler._bgm_stream.close()
        AudioHandler._bgm_stream = stream
        threading.Thread(target=AudioHandler.play_stream, args=(AudioHandler._bgm_stream,)).start()
        threading.Thread(target=AudioHandler._loop_bgm, args=(source,)).start()

    @staticmethod
    def play_sfx(source):
        stream = AudioHandler.get_stream(source)
        threading.Thread(target=AudioHandler.play_stream, args=(stream,))

    @staticmethod
    def close():
        AudioHandler._bgm_stream.close()
        for s in AudioHandler._sfx_streams:
            s.close()
        AudioHandler._bgm_track = None
        AudioHandler._sfx_tracks = []
        AudioHandler._closed = True
        AudioHandler._p.terminate()
