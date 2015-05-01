import time
import wave
import pyaudio


class Tick(object):

    CHUNK = 1024

    def __init__(self, beats_per_min=None, wav_file=None):
        self._beats_per_min = beats_per_min

        sound = wave.open(wav_file)
        try:
            player = pyaudio.PyAudio()
            self._stream = player.open(
                format=player.get_format_from_width(sound.getsampwidth()),
                channels=sound.getnchannels(),
                rate=sound.getframerate(),
                output=True)
            self._data = sound.readframes(Tick.CHUNK)
        finally:
            sound.close()

    def set_beats_per_min(self, v):
        print("bpm={bpm}".format(bpm=v))
        self._beats_per_min = v

    def toc(self):
        before = time.time()
        self._stream.write(self._data)
        after = time.time()
        dt = after - before
        time.sleep(60. / self._beats_per_min - dt)


def start_metronome(beats_per_min, ticks=None, mins=None, speed_up=-1, upper_limit=-1, wav_file='beep.wav'):

    tick = Tick(wav_file=wav_file)
    while True:

        tick.set_beats_per_min(beats_per_min)

        if ticks is not None:
            for x in range(ticks):
                tick.toc()

        elif mins is not None:
            start = time.time()
            while True:
                tick.toc()
                now = time.time()
                if (now - start) / 60. > mins:
                    break

        beats_per_min += speed_up

        if beats_per_min > upper_limit:
            break