from typing import Union

import pretty_midi
from itertools import groupby

SUSTAIN_PEDAL_CONTROLLER_NUMBER: int = 64


class SustainRange:
    """
    Simple class to describe an interval of time during which the sustain pedal was on. `start` corresponds to the
    time of a sustain pedal on message, and `stop` corresponds to the time of the next sustain pedal off message.
    """

    def __init__(self, start: Union[int, float], stop: Union[int, float]):
        """
        Create a sustain range
        :param start: time of a sustain pedal on message
        :param stop: time of the sustain pedal off message coming right after the time of `start`
        """
        self.start: Union[int, float] = start
        self.stop: Union[int, float] = stop

    def contains(self, time: Union[int, float]) -> bool:
        """
        Returns True if the passed time is in the range, else returns False
        :param time: time to check
        :return: boolean
        """
        return self.start < time <= self.stop

    def __str__(self):
        return f"({self.start}, {self.stop})"

    def __eq__(self, other):
        return self.start == other.start and self.stop == other.stop


def get_all_sustain_ranges(midi_track: pretty_midi.Instrument) -> list[SustainRange]:
    """
    Get the sustain ranges for the given track
    :param midi_track: input midi track
    :return: list of all the sustain ranges of the track
    """

    def is_sustain_pedal(m: pretty_midi.ControlChange):
        return m.number == SUSTAIN_PEDAL_CONTROLLER_NUMBER

    def is_sustain_pedal_on(m: pretty_midi.ControlChange): return is_sustain_pedal(m) and m.value >= 64
    def is_sustain_pedal_off(m: pretty_midi.ControlChange): return is_sustain_pedal(m) and not is_sustain_pedal_on(m)

    sustain_ranges = []
    start = None
    stop = None
    for message in midi_track.control_changes:
        if is_sustain_pedal_on(message) and start is None:
            start = message.time
        elif is_sustain_pedal_off(message) and start is not None:
            stop = message.time
        if start is not None and stop is not None:
            sustain_ranges.append(SustainRange(start, stop))
            start = None
            stop = None
    if start is not None:
        sustain_ranges.append(SustainRange(start, max(midi_track.notes, key=lambda n: n.end).end))
    return sustain_ranges


def extend_notes_in_range(midi_track: pretty_midi.Instrument, sustain_range: SustainRange):
    """
    Extend the length of the notes in the given midi track until the stop of the sustain range.
    :param midi_track: input midi track
    :param sustain_range: Range to apply to the midi track
    :return: None, `midi_track` is modified
    """

    def is_in_range(m: pretty_midi.Note) -> bool: return sustain_range.contains(m.end)
    for note in filter(is_in_range, midi_track.notes):
        note.end = sustain_range.stop


def remove_overlapping_notes(midi_track: pretty_midi.Instrument):
    """
    Remove overlapping notes of the same pitch in the midi track.
    :param midi_track: input midi track
    :return: None, `midi_track` is modified
    """
    sorted_notes = sorted(midi_track.notes, key=lambda n: n.pitch)
    for _, notes in groupby(sorted_notes, key=lambda n: n.pitch):
        notes = sorted(list(notes), key=lambda x: x.start)
        for i in range(len(notes) - 1):
            if notes[i + 1].start < notes[i].end:
                notes[i].end = notes[i+1].start


def sustain(midi_file: pretty_midi.PrettyMIDI):
    """
    Convert the sustain pedal events of the midi file to longer notes. This is applied to all tracks individually.
    :param midi_file: input midi file
    :return: None, `midi_file` is modified
    """
    for track in midi_file.instruments:
        for sustain_range in get_all_sustain_ranges(track):
            extend_notes_in_range(track, sustain_range)
        remove_overlapping_notes(track)


def sustain_file(input_file: str, output_file: str):
    """
    Convert the sustain pedal events of the midi file `input_file` and save the result in `output_file`
    :param input_file: Path to the input MIDI file
    :param output_file: Path to the output MIDI file. If the file exists, it's overwritten.
    :return: None
    """
    midi = pretty_midi.PrettyMIDI(input_file)
    sustain(midi)
    midi.write(output_file)

