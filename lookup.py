import sys
from process import *
from models import *

def main(file_path, *octave):
	csv_path = hum_csv_path + process(file_path)
	hum = Hum(csv_path)
	if len(octave) > 0:
		matches = hum.get_matches(octave[0])
	else:
		matches = hum.get_matches()
	print "Best"
	for x in xrange(0,len(matches)):
		song = matches[x]
		print str(x+1) + ". " + title_from_path(song[0])


if len(sys.argv) > 2:
	main(sys.argv[1], sys.argv[2])
else:
	main(sys.argv[1])
