import wave
from analyze import *

class Song:
"""
Represents a song, that, when initialized, generates the spectrograph, the array of 
intense parts, has a method that can be called to insert the song into the database
"""
	def __init__(self,file_path):
		self.file_path = file_path
		self.gen_melody
		return

	# stores the tuple list of (time,midi_val) from the file path in melody
	def gen_melody(self):
		self.melody = get_melody(file_path)
		return

	# returns top 10 matches
	def get_matches(self):
		# some code here ab

