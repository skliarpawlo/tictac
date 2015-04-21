import timeit


def test_accuracy():
    res = timeit.timeit(
        "start_metronome(beats_per_min=60, ticks=5, speed_up=10, upper_limit=60)",
        setup="from tictoc import start_metronome",
        number=2,
    )
    assert abs(res - 10.) < 0.1