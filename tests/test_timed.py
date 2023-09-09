import mock
import sustain_to_longer_notes.core as sus


def test_timed():
    expected = zip(mock.Data.TIMED.tracks[0], [10, 20, 65, 70, 81])
    timed = sus.timed(mock.Data.TIMED.tracks[0])
    for expect, actual in zip(expected, timed):
        assert expect[0] == actual[0]
        assert expect[1] == actual[1]
