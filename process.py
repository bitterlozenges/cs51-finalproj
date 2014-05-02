# process a single audio file into .csv using Melodia

from sys import *
from subprocess import *
from os import *
from string import *
from models import title_from_path
import platform

# input_path is a folder if Hum = False
# input_path is a filename if Hum = True
# input_path should be unix filepath with "/" not "\"; if error, place hum audio file in the same directory as this python file
def process(input_path, Hum=True):
	# output filepath, needed to pull .csv file for matching
	output_path = title_from_path(input_path) + "_vamp_mtg-melodia_melodia_melody.csv"

	# default database for Hums
	db_path = "hum_database"

	# if not Hum, change database path and recurse through song directory
	if Hum == False:
		db_path = "song_database"
		input_path = input_path + " -r"

	# check platform for Windows or Darwin (OSX), and change command-line command as necessary
	platform_name = platform.platform()
	if "Darwin" in platform_name:
		os_path = "sonic_annotator/sonic-annotator"
	elif "Windows" in platform_name: 
		os_path = ".\sonic_annotator\sonic-annotator"
	else:
		os_path = "sonic_annotator/sonic-annotator"

	# build shell argument
	shell_arg = os_path + " -d vamp:mtg-melodia:melodia:melody " + input_path + " -w csv --csv-basedir " + db_path

	# code obtained from subprocess documentation 
	# https://docs.python.org/2/library/subprocess.html#module-subprocess
	# runs shell argument
	try:
	    retcode = call(shell_arg, shell=True)
	    if retcode < 0:
	        print >>sys.stderr, "Child was terminated by signal", -retcode
	    return output_path
	except OSError as e:
	    print >>sys.stderr, "Execution failed:", e
