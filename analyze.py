#analysis of song file module

#from the filepath 'file' and return the filepath to a new file containing the melody information
def get_melody(file):
	raise Exception('Not implemented')

#from the melody file, generate an array of midi values collected at regular intervals
def process_melody(melody):
	raise Exception('Not implemented')

def freq_to_midi(freq):
	return 69 + 12*math.log[(freq/440),2]

