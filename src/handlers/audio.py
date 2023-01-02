import time
import wave
import threading
import pyaudio

CHUNK = 1024


class AudioHandler:
    volume = 100
    muted = False
    _p = pyaudio.PyAudio()
    _bgm_stream: pyaudio.Stream = None
    _sfx_streams: [pyaudio.Stream] = []

    def __del__(self):
        AudioHandler.stop_audio()
        AudioHandler._bgm_track = None
        AudioHandler._sfx_tracks = []

    @staticmethod
    def get_stream(source):
        def cb(in_data, frame_count, time_info, status):
            data = wf.readframes(frame_count)
            return data, pyaudio.paContinue

        wf = wave.open(source, 'rb')
        p = AudioHandler._p
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True,
                        stream_callback=cb
                        )
        return stream

    @staticmethod
    def play_stream(stream):
        while stream.is_active():
            time.sleep(0.1)
        stream.close()

    @staticmethod
    def loop_bgm():
        while True:
            if AudioHandler._bgm_stream and not AudioHandler._bgm_stream.is_active():
                AudioHandler._bgm_stream.start_stream()

    @staticmethod
    def play_bgm(source):
        stream = AudioHandler.get_stream(source)
        if AudioHandler._bgm_stream:
            AudioHandler._bgm_stream.close()
        AudioHandler._bgm_stream = stream
        threading.Thread(target=AudioHandler.play_stream, args=(AudioHandler._bgm_stream,))

    @staticmethod
    def play_sfx(source):
        stream = AudioHandler.get_stream(source)


    @staticmethod
    def stop_audio():
        AudioHandler._bgm_stream.close()
        for s in AudioHandler._sfx_streams:
            s.close()
