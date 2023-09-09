import mido

SUSTAIN_PEDAL_CONTROLLER_NUMBER: int = 64


class SustainRange:
    """
    Simple class to describe an interval of time during which the sustain pedal was on. `start` corresponds to the
    time of a sustain pedal on message, and `stop` corresponds to the time of the next sustain pedal off message.
    """

    def __init__(self, start: int | float, stop: int | float):
        """
        Create a sustain range
        :param start: time of a sustain pedal on message
        :param stop: time of the sustain pedal off message coming right after the time of `start`
        """
        self.start: int | float = start
        self.stop: int | float = stop

    def contains(self, time: int | float) -> bool:
        """
        Returns True if the passed time is in the range, else returns False
        :param time: time to check
        :return: boolean
        """
        return self.start <= time <= self.stop

    def __str__(self):
        return f"({self.start}, {self.stop})"

    def __eq__(self, other):
        return self.start == other.start and self.stop == other.stop


def timed(midi_track: mido.MidiTrack) -> zip:
    """
    Returns a zip of midi track along with the absolute time of each message
    :param midi_track: input midi track
    :return:
    """
    time = 0
    times = [m.time for m in midi_track]
    for i, t in enumerate(times):
        time += t
        times[i] = time
    return zip(midi_track, times)


def get_all_sustain_ranges(midi_track: mido.MidiTrack) -> list[SustainRange]:
    """
    Get the sustain ranges for the given track
    :param midi_track: input midi track
    :return: list of all the sustain ranges of the track
    """

    def is_sustain_pedal(m: mido.Message):
        return m.type == "control_change" and m.control == SUSTAIN_PEDAL_CONTROLLER_NUMBER

    def is_sustain_pedal_on(m: mido.Message): return is_sustain_pedal(m) and m.value >= 64
    def is_sustain_pedal_off(m: mido.Message): return is_sustain_pedal(m) and not is_sustain_pedal_on(m)

    sustain_ranges = []
    start = None
    stop = None
    for message, time in filter(lambda x: is_sustain_pedal(x[0]), timed(midi_track)):
        if is_sustain_pedal_on(message) and start is None:
            start = time
        elif is_sustain_pedal_off(message) and start is not None:
            stop = time
        if start is not None and stop is not None:
            sustain_ranges.append(SustainRange(start, stop))
            start = None
            stop = None
    if start is not None:
        sustain_ranges.append(SustainRange(start, list(timed(midi_track))[-1][1]))
    return sustain_ranges


def extend_notes_in_range(midi_track: mido.MidiTrack, sustain_range: SustainRange):
    """
    Extend the length of the notes in the given midi track until the stop of the sustain range.
    :param midi_track: input midi track
    :param sustain_range:
    """

    def is_in_range(m: mido.Message) -> bool: return sustain_range.contains(m.time)
    def is_note_off(m: mido.Message) -> bool: return m.type == 'note_off' or m.type == 'note_on' and m.velocity == 0
    def filter_func(m: mido.Message) -> bool: return is_in_range(m) and is_note_off(m)
    for message in filter(filter_func, midi_track):
        message.time = sustain_range.stop


def remove_overlapping_events(midi_track: mido.MidiTrack):
    pass


def sustain(midi_file: mido.MidiFile):
    for track in midi_file.tracks:
        pass
