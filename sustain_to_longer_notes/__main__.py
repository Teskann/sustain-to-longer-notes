import os.path
import sys
import argparse
from os.path import isdir, isfile, splitext
import glob
from core import sustain_file


def main(args):
    parser = argparse.ArgumentParser(description="Convert the sustain pedal MIDI events to longer notes.")
    parser.add_argument("file",
                        help="Input MIDI file(s) to convert. The output file name(s) are the same as input but "
                             "suffixed by '_sustained'.",
                        nargs="+")

    parsed_args = parser.parse_args(args)
    inputs = parsed_args.file
    files = []
    for input_file in inputs:
        if isdir(input_file):
            files += glob.glob(args.input + '/*.[Mm][Ii][Dd]')
        elif isfile(input_file):
            files.append(input_file)
        else:
            raise FileNotFoundError(f"No such file or directory `{input_file}`.")

    for file in files:
        split = os.path.splitext(file)
        output_file_name = split[0] + "_sustained" + split[1]
        sustain_file(file, output_file_name)


if __name__ == "__main__":
    main(sys.argv[1:])
