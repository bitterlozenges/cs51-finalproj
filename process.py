# process.py
# processes a directory of .wav files into .csv melody extracted
# python process.py song_path

import sys
import string
import os
import subprocess

# get directory containing songs we wish to process
# and parent directory for storage
song_dir = str(sys.argv[1])

shell_arg = ".\sonic_annotator\sonic-annotator -d vamp:mtg-melodia:melodia:melody " + song_dir + " -r -w csv --csv-basedir song_database"

# code obtained from subprocess documentation 
# https://docs.python.org/2/library/subprocess.html#module-subprocess
try:
    retcode = subprocess.call(shell_arg, shell=True)
    if retcode < 0:
        print >>sys.stderr, "Child was terminated by signal", -retcode
except OSError as e:
    print >>sys.stderr, "Execution failed:", e