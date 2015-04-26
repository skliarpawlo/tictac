import argparse

arg_parser = argparse.ArgumentParser(
    description="Simple stupid metronome"
)

arg_parser.add_argument('--bpm', type=int, default=60, help='beats per minute')
arg_parser.add_argument('--mins', type=float, default=2, help='minutes, each set lasts')
arg_parser.add_argument('--speed-up', type=int, default=5, help='speed up after each set ends')
arg_parser.add_argument('--upper-limit', type=int, default=120, help='upper limit of beats per minute, when to stop')
