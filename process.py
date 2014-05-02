# process a single audio file into .csv using Melodia

from sys import *
from subprocess import *
from os import *
from string import *

# input_path is a folder if Hum = False
# input_path is a filename if Hum = True
# input_path should be unix filepath with "/" not "\"; if error, place hum audio file in the same directory as this python file
def process(input_path, Hum=True):
	db_path = "hum_database"
	if Hum == False:
		db_path = "song_database"
		input_path = input_path + " -r"

	shell_arg = ".\sonic_annotator\sonic-annotator -d vamp:mtg-melodia:melodia:melody " + input_path + " -w csv --csv-basedir " + db_path
	
	# code obtained from subprocess documentation 
	# https://docs.python.org/2/library/subprocess.html#module-subprocess
	try:
	    retcode = call(shell_arg, shell=True)
	    if retcode < 0:
	        print >>sys.stderr, "Child was terminated by signal", -retcode
	except OSError as e:
	    print >>sys.stderr, "Execution failed:", e