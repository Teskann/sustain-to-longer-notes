import mock
import sustain_to_longer_notes.core as sus


def test_c_scale_no_sustain():
    track = mock.Data.C_SCALE_NO_SUSTAIN.tracks[0]
    assert sus.get_all_sustain_ranges(track) == []


def test_one_track():
    expected = [sus.SustainRange(1920, 3600), sus.SustainRange(3840, 4080)]
    track = mock.Data.ONE_TRACK.tracks[0]
    assert sus.get_all_sustain_ranges(track) == expected


def test_one_track_no_stop():
    expected = [sus.SustainRange(1920, 3600), sus.SustainRange(3840, 4080)]
    track = mock.Data.ONE_TRACK_NO_STOP.tracks[0]
    assert sus.get_all_sustain_ranges(track) == expected
