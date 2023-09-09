import os

import pretty_midi
from os.path import join, abspath, dirname


class Data:
    pass


DATA_FILES_PATH = join(abspath(dirname(__file__)), "midi")
for file in os.listdir(DATA_FILES_PATH):
    setattr(Data, file.split(".")[0], pretty_midi.PrettyMIDI(join(DATA_FILES_PATH, file)))
