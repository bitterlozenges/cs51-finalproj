#analysis of song file module
#library for working with csvs
import csv
import sys
import math

#constant for how long a pause should be before considering it a start point
pause = 2.0



#from the filepath 'file', return a (float,float) array containing the melody information
def get_melody(file):
	melody_array = []
	with open(file,"rb") as raw_melody:
		reader = csv.reader(raw_melody)
		for row in reader:
			tick = (float(row[0]),float(row[1]))
			melody_array.append(tick)
	return melody_array

#from the melody file, generate a float array of midi values collected at regular intervals
def process_melody(melody):
	midi_array = []
	diff_array = []	
	# strip all leading zeroes
	if melody[0][1] <= 0:
		while melody[0][1] <= 0:
			melody.remove(melody[0])
	# iterate over melody, zero negative frequencies and store as midi values			
	for tick in melody:
		timescale = tick[0]
		frequency = tick[1]
		new_tick = (timescale,freq_to_midi(frequency))
		midi_array.append(new_tick)	
	# get first differences of midi array	
	for x in xrange(0,len(midi_array)-1):
		time1,freq1 = midi_array[x]
		time2,freq2 = midi_array[x+1]
		diff_array.append((time1,freq2-freq1))
	return (midi_array, diff_array)

"""
from the melody array, returns int array of indicies of start points which 
represent beginning of melodic lines
note: here we are using the constant of 2 seconds pause = end of melodic line
"""
def get_starts(melody):
	len_silence = 0.0
	last_melody = 0.0
	starts = []
	for x in xrange(0,len(melody)):
		if melody[x][1] > 0:
			if len_silence > pause:
				starts.append(x)
			len_silence = 0.0
			last_melody = melody[x][0]
		else: 
			len_silence = melody[x][0] - last_melody 				
	return starts			

# from a float freq return the corresponding float for midi value
def freq_to_midi(freq):
	if freq < 0:
		return 0
	else:
		return 69 + 12*math.log((freq/440),2)
