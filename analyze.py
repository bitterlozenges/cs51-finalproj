#analysis of song file module
#library for working with csvs
import csv

#from the filepath 'file' and return an array containing the melody information
def get_melody(file):
	melody_array = []
	with open('file','rb') as raw_melody
	reader = csv.reader(raw_melody)
	for row in reader:
		timestamp,frequency = row
		melody_array.append(timestamp,frequency)
	return melody_array

#from the melody file, generate an array of midi values collected at regular intervals
def process_melody(melody):
	midi_array = []
	diff_array = []	
	for (timestamp,frequency) in melody:
		if frequency < 0:
			frequency = 0
		midi_array.append(timestamp,freq_to_midi(frequency))
	for x in xrange(0,len(midi_array)):
		time1,freq1 = midi_array.x 
		time2,freq2 = midi_array.(x+1)
		diff_array.append((time1,freq2-freq1))
	raise Exception('Not implemented')

def freq_to_midi(freq):
	return 69 + 12*math.log[(freq/440),2]

