#analysis of song file module
#library for working with csvs
import csv
import sys
import math

#constant for how long a pause should be before considering it a start point
ticks_per_second = 338 // 3
compression_factor = 5

# from the filepath 'file', return a (float,float) array containing the melody 
# information in the form of (timescale, midiscore)
def get_midi(file):
	midi_array = []
	with open(file,"rb") as raw_melody:
		reader = csv.reader(raw_melody)
		
		for row in reader:
			# converts frequency to midi score, handles negs by subbing in zeros
			tick = (float(row[0]),freq_to_midi(float(row[1])))
			midi_array.append(tick)

		# strips leading 0s
		while midi_array[0][1] == 0:
			del midi_array[0]
		# chooses every compression_factor-th midi score 
		midi_array = midi_array[0::compression_factor]		
	return midi_array

# from the midi array, generate a float array of midi value differences
# collected at regular intervals
def diffs_midi(midi):
	diff_array = []	
	# get first differences of midi array	
	for x in xrange(0,len(midi)-1):
		time1,freq1 = midi[x]
		time2,freq2 = midi[x+1]
		diff_array.append((time1,freq2-freq1))
	return diff_array


# from the midi array, returns int array of indicies of start points which 
# represent beginning of melodic lines here we are using the constant of 1 
# start every 338/2 points = 0.5 seconds
def get_starts(midi):
	starts = []
	for x in xrange(0,len(midi) // ticks_per_second):
		starts.append(x * ticks_per_second)		
	return starts

# from a float freq return the corresponding float for midi value
def freq_to_midi(freq):
	if freq <= 0:
		return 0
	else:
		return 69 + 12*math.log((freq/440),2)
