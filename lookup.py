import sys
from process import process
from models import *

def main(file_path, *octave):
	csv_path = "hum_database/" + process(file_path)
	hum = Hum(csv_path)
	if len(octave) > 0:
		matches = hum.get_matches(octave[0])
	else:
		matches = hum.get_matches()
	print "Best"
	for x in xrange(0,len(matches)):
		song = matches[x]
		print (str(x+1) + ". " + title_from_path(song[0]), song[1])


if len(sys.argv) > 2:
	main(sys.argv[1], sys.argv[2])
else:
	main(sys.argv[1])
