import sys
import argparse
import os
from process import *
from models import *
from database import db_session

# argument parser to ensure octaves is an integer, and that filepath is a string, and a optional db flag to display database"
parser = argparse.ArgumentParser(description='Matches an audio file to the database.')
parser.add_argument("--path", dest="path", metavar="path", type = str, help="A filepath for the hum audio file you wish to match.")
parser.add_argument("--oct", dest="octaves", metavar="octaves", type = int, help="An integer number of octaves.", default=0)
parser.add_argument("--db", action = "store_true", help="Displays the songs in your database.")

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

if args.db:
	songs = db_session.query(Song).all()
	print "Songs in your database:"
	for song in songs:
		print title_from_path(song.file_path)
elif args.path == None: 
	print "Please execute 'python lookup.py -h' for help, and enter a valid filepath."
else:
	main(args.path,args.octaves)