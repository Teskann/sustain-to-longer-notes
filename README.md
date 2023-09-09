# Sustain to Longer Notes

Convert a MIDI file with sustain pedal events to a midi file with
changed notes duration.

## Installation

### Prerequisites
* 
* Python 3
* Make

### Install command

```commandline
make
```

## Usage

```
usage: sustain [-h] file [file ...]

Convert the sustain pedal MIDI events to longer notes.

positional arguments:
  file        Input MIDI file(s) to convert. The output file name(s) are the same as input but suffixed by '_sustained'.

options:
  -h, --help  show this help message and exit
```
