#!/usr/bin/env python

from utils.arg_parse import arg_parser
from utils.metr import start_metronome


if __name__ == '__main__':
    args = arg_parser.parse_args()
    start_metronome(
        beats_per_min=args.bpm,
        mins=args.mins,
        speed_up=args.speed_up,
        upper_limit=args.upper_limit,
        wav_file=args.wav,
    )