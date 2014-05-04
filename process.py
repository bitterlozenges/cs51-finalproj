# process a single audio file into .csv using Melodia

from sys import *
from subprocess import *
from os import *
from string import *
from models import *
import platform

# default path for folder containing .csv files for our song database
song_csv_path = "song_csv/"

# default path for folder containing .csv files for our hums
hum_csv_path = "hum_csv/"

# input_path is a folder if Hum = False
# input_path is a filename if Hum = True
# place hum audio file in the same directory as this python file
def process(input_path, Hum=True):
	# output filepath, needed to pull .csv file for matching
	# melodia plugin adds the tag below to each .csv
	output_path = title_from_path(input_path) + melodia_tag

	# adds "" around input path to ensure the path works in shell
	input_path = '"' + input_path + '"'

	# if not Hum, change database folder path (folder containing .csv files) and recurse through song directory provided
	if Hum == False:
		db_path = song_csv_path
		input_path = input_path + " -r"
	else:
		# default .csv folder for Hums
		db_path = hum_csv_path

	# check platform for Windows or Darwin (OSX), and change command-line command as necessary
	platform_name = platform.platform()
	if "Darwin" in platform_name:
		os_path = "sonic_annotator/sonic-annotator-mac"
	elif "Windows" in platform_name: 
		os_path = ".\sonic_annotator\sonic-annotator"
	else:
		os_path = "sonic_annotator/sonic-annotator"

	# build shell argument
	shell_arg = os_path + " -d vamp:mtg-melodia:melodia:melody " + input_path + " -w csv --csv-basedir " + db_path
	print shell_arg

	# code obtained from subprocess documentation 
	# https://docs.python.org/2/library/subprocess.html#module-subprocess
	# runs shell argument for Sonic Annotator
	try:
	    retcode = call(shell_arg, shell=True)
	    if retcode < 0:
	        print >>sys.stderr, "Child was terminated by signal", -retcode
	    return output_path
	except OSError as e:
	    print >>sys.stderr, "Execution failed:", e
