from os.path import join, abspath, dirname
from sustain_to_longer_notes.core import sustain_file
import filecmp


def test_sustain_file():
    HERE = dirname(abspath(__file__))
    input_file = join(HERE, "midi", "MULTI_TRACK.mid")
    output_file = join(HERE, "midi", "MULTI_TRACK_exported.mid")
    sustain_file(input_file, output_file)
    assert filecmp.cmp(output_file, join(HERE, "expected_midi", "MULTI_TRACK_sustained.mid"))
