import wave
from analyze import *
from database import 


class Song:
	"""
	Represents a song, that, when initialized, generates the spectrograph, the array of 
	intense parts, has a method that can be called to insert the song into the database
	"""
	def __init__(self,file_path,melody=None,starts=None):
		self.file_path = file_path
		# if the melody parameter was not passed, generate it
		if melody == None:
			self.gen_melody()
		else:
			self.melody = melody
		# if the starts parameter was not passed, generate it.
		if starts == None:
			self.gen_starts()
		else:
			self.starts = starts
		return

	# stores the tuple list of (time,midi_val) from the file path in melody
	def gen_melody(self):
		self.melody = get_melody(file_path)
		return

	# from a given melody, generates the "starts"
	def gen_starts(self):
		self.starts = get_starts(self.melody)
		return

	# returns top 10 matches
	def get_matches(self):
		dict_songs = {}
		# some code here about getting the melody
		#for row in songs
		#	song = to_song(row['object'])
		#	for start in song.starts
		#	do the frechet distance
		#	store the song name and frechet distance stuff
		# get the top 10 shortest lengths of song in the dictionary
		return

# object hook for getting a song object from a json string
def as_song(dic):
	file_path = dic['file_path']
	melody = dic['melody']
	starts = dic['starts']
	return Song(file_path,melody,starts)

# returns a song given a json string
def to_song(str):
	return json.loads(str,object_hook=as_song)
