import argparse


def main():
    parser = argparse.ArgumentParser(description="Convert the sustain pedal MIDI events to longer notes.")
    parser.add_argument("file", help="Input MIDI file(s) to convert", nargs="?")
    parser.add_argument("-o", "--output-file", nargs="?",
                        help="Output MIDI file, converted. If you don't use this argument, the input files will be "
                             "overwritten.")
    