import pyaudio
import wave
import time


class Tick(object):

    CHUNK = 1024

    def __init__(self, beats_per_min=None):
        self._beats_per_min = beats_per_min

        sound = wave.open("beep.wav")
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
        self._beats_per_min = v

    def toc(self):
        before = time.time()
        self._stream.write(self._data)
        after = time.time()
        dt = after - before
        time.sleep(60. / self._beats_per_min - dt)


def start_metronome(beats_per_min, ticks=None, mins=None, speed_up=-1, upper_limit=-1):

    tick = Tick()
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


if __name__ == '__main__':
    start_metronome(beats_per_min=60, mins=0.1, speed_up=10, upper_limit=120)