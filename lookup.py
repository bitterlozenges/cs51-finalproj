import sys
import argparse
import os
from process import *
from models import *


# argument parser to ensure octaves is an integer, and that filepath is a string
parser = argparse.ArgumentParser(description='Matches an audio file to the database.')
parser.add_argument("path", metavar="path", type = str, help="A filepath for the hum audio file you wish to match.")
parser.add_argument("--oct", dest="octaves", metavar="octaves", type = int, help="An integer number of octaves.", default=0)


args = parser.parse_args()

def main(file_path, *octave):
	csv_path = hum_csv_path + process(file_path.replace("\\","/"))
	hum = Hum(csv_path)
	if len(octave) > 0:
		matches = hum.get_matches(float(octave[0]))
	else:
		matches = hum.get_matches()
	print "Best"
	for x in xrange(0,len(matches)):
		song = matches[x]
		print str(x+1) + ". " + title_from_path(song[0])

main(args.path,args.octaves)
'''
if len(sys.argv) > 2:
	main(sys.argv[1],sys.argv[2])
else:
	main(sys.argv[1])
'''