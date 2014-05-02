#analysis of song file module
#library for working with csvs
import csv
import sys
import math

#constant for how long a pause should be before considering it a start point
blip = 5.0
len_pause = 2.0
len_start = 0.25
pause = 0.5
ticks_per_second = 338



#from the filepath 'file', return a (float,float) array containing the melody information
# in the form of (timescale, midiscore)
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
				
	return midi_array

#from the midi array, generate a float array of midi value differences collected at regular intervals
def diffs_midi(midi):
	diff_array = []	
	# get first differences of midi array	
	for x in xrange(0,len(midi)-1):
		time1,freq1 = midi[x]
		time2,freq2 = midi[x+1]
		diff_array.append((time1,freq2-freq1))
	return diff_array

"""
from the midi array, returns int array of indicies of start points which 
represent beginning of melodic lines
note: here we are using the constant of 0.5 seconds pause = end of melodic line
"""
def get_starts(midi):
	len_silence = 0.0
	len_sound = 0.0
	last_melody = 0.0
	last_silence = 0.0
	check = False
	starts = [0]
	for x in xrange(0,len(midi)):
		if midi[x][1] > 0:
			if len_silence > pause and (len_sound > blip):
				starts.append(x)
				len_silence = 0.0
			elif len_silence <= pause and (len_sound > blip):
				len_silence = 0.0
			last_melody = midi[x][0]
			len_sound = midi[x][0] - last_silence
		else:
			len_sound = 0.0 
			len_silence = midi[x][0] - last_melody
			last_silence = midi[x][0] 				
	return starts
	"""
	len_silence = 0.0
	last_melody = 0.0
	starts = [0]
	for x in xrange(0,len(midi)):
		if midi[x][1] > 0:
			if len_silence > pause:
				starts.append(x)
			len_silence = 0.0
			last_melody = midi[x][0]
		else: 
			len_silence = midi[x][0] - last_melody 				
	return starts
	"""					

# from a float freq return the corresponding float for midi value
def freq_to_midi(freq):
	if freq <= 0:
		return 0
	else:
		return 69 + 12*math.log((freq/440),2)
