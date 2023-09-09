import mock
from sustain_to_longer_notes.core import extend_notes_in_range, SustainRange


def test_0_10():
    track = mock.Data.ONE_TRACK.instruments[0]
    extend_notes_in_range(track, SustainRange(0, 10))
    for note in track.notes:
        assert note.end == 10


def test_0_3():
    track = mock.Data.ONE_TRACK.instruments[0]
    extend_notes_in_range(track, SustainRange(0, 3.0))
    for note in track.notes:
        assert note.end == 3.0 or note.end > 3.0


def test_2_10():
    track = mock.Data.ONE_TRACK.instruments[0]
    extend_notes_in_range(track, SustainRange(2.0, 10.0))
    for note in track.notes:
        assert note.end == 10 or note.end < 2.0
