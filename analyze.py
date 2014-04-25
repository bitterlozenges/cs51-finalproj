#analysis of song file module
#library for working with csvs
import csv
import sys

#from the filepath 'file' and return an array containing the melody information
def get_melody(file):
	melody_array = []
	with open(file,"rb") as raw_melody:
		reader = csv.reader(raw_melody)
		for row in reader:
			tick = (row[0],row[1])
			melody_array.append(tick)
	print melody_array
	return melody_array

#from the melody file, generate an array of midi values collected at regular intervals
def process_melody(melody):
	midi_array = []
	diff_array = []	
	# strip all leading zeroes
	if melody[0][1] <= 0:
		for x in xrange(0,len(melody))
			if melody[x][1] > 0:
				break 
			else
				melody.remove(melody[x])		
	for x in xrange			
	# iterate over melody, zero negative frequencies and store as midi values			
	for tick in melody:
		timescale = tick[0]
		frequency = tick[1]
		if frequency < 0:
			frequency = 0
		midi_array.append(timescale,freq_to_midi(frequency))	
	# get first differences of midi array	
	for x in xrange(0,len(midi_array)):
		time1,freq1 = midi_array[x]
		print midi_array[x]
		time2,freq2 = midi_array[x+1]
		diff_array.append((time1,freq2-freq1))
	raise Exception('Not implemented')
# from the melody array, selects start points which represent beginning of melodic lines
def gen_starts(melody):

	
def freq_to_midi(freq):
	return 69 + 12*math.log[(freq/440),2]
