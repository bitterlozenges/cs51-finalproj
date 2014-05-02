import sys
from process import process
from models import *

def main(file_path):
	csv_path = process(file_path)
	hum = Hum(csv_path)
	matches = hum.get_matches()
	print "Best"
	for x in xrange(0,len(matches)):
		song = matches[x]
		print title_from_path(song.file_path)

main(sys.argv[1])
