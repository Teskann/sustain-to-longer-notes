import mock
import copy
from sustain_to_longer_notes.core import remove_overlapping_notes


def test_overlapping_notes():
    track = mock.Data.OVERLAPPING_NOTES.instruments[0]
    expected_track = copy.deepcopy(track)
    expected_ends = [1, 1.5, 1, 1.25, 1.5, 1.75]
    remove_overlapping_notes(track)
    for i, note in enumerate(track.notes):
        assert note.pitch == expected_track.notes[i].pitch
        assert note.velocity == expected_track.notes[i].velocity
        assert note.start == expected_track.notes[i].start
        assert note.end == expected_ends[i]
