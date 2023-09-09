import os
from os.path import abspath, join, dirname
import py_midicsv
import shutil


HERE = abspath(dirname(__file__))


def clear_test_data():
    if os.path.exists(join(HERE, "midi")):
        shutil.rmtree(join(HERE, "midi"))


def create_test_data():
    midi_path = join(HERE, "midi")
    csv_path = join(HERE, "csv")
    os.mkdir(midi_path)
    for file in os.listdir(csv_path):
        midi = py_midicsv.csv_to_midi(join(csv_path, file))
        with open(join(midi_path, file.split(".")[0] + ".mid"), "wb") as f:
            midi_writer = py_midicsv.FileWriter(f)
            midi_writer.write(midi)
