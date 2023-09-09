import os

import mido
from os.path import join, abspath, dirname


class Data:
    EMPTY_FILE = mido.MidiFile()


DATA_FILES_PATH = join(abspath(dirname(__file__)), "midi")
for file in os.listdir(DATA_FILES_PATH):
    setattr(Data, file.split(".")[0], mido.MidiFile(join(DATA_FILES_PATH, file)))
