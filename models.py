from sqlalchemy import Table, Column, Integer, String, Text
from sqlalchemy.orm import mapper
import json
from database import db_session, metadata
from analyze import *
#for the split function
import ntpath
from distance import frechet

# melodia filename tag
melodia_tag = "_vamp_mtg-melodia_melodia_melody.csv"

class Music(object):
	def __init__(self,file_path,melody=None,diffs=None):
		self.file_path = file_path

		# if the melody parameter was not passed, generate it
		if melody == None:
			self.gen_melody()
		else:
			self.melody = melody
		# if the melody parameter was not passed, generate it
		if diffs == None:
			self.gen_diffs()
		else:
			self.diffs = diffs

		return

	# generates the melody from the file_path and stores as a json string
	def gen_melody(self):
		self.melody = json.dumps(get_midi(self.file_path))
		return

	# stores the first differences as a json string	
	def gen_diffs(self):
		self.diffs = json.dumps(diffs_midi(json.loads(self.melody)))
		return

	

class Song(Music):
	"""
	Represents a song, that, when initialized, generates the main melody, the start
	points of a song, and generates the difference array
	"""
	def __init__(self,file_path,melody=None,diffs=None,starts=None):

		Music.__init__(self,file_path,melody,diffs)
		
		# if the starts parameter was not passed, generate it.
		if starts == None:
			self.gen_starts()
		else:
			self.starts = starts
		return

	# array of indices at which start points occur
	def gen_starts(self):
		self.starts = json.dumps(get_starts(json.loads(self.melody)))
		return

songs = Table('songs', metadata,
    Column('id', Integer, primary_key=True),
    Column('file_path', String(100), unique=True),
    Column('melody', Text),
    Column('diffs', Text),
    Column('starts', Text)
)

mapper(Song, songs)


class Hum(Music):
	"""
	Represents a clip of someone humming that extends the Music class
	with extra functionality of getting music
	"""
	# returns top 10 matches with optional octave displacement
	def get_matches(self, octave=0):
		# gets dictionary of songs
		dict_songs = db_session.query(Song).all()
		song_diffs = []

		def melody_transpose(melody):
			# function for transposing a tick by octave octaves 
			def tick_transpose(tick, octave):
				if tick[1] == 0:
					return tick
				new_midi = (float(octave) * 12) + tick[1]
				return (tick[0],new_midi)
			
			new_melody = []
			for tick in melody:
				new_melody.append(tick_transpose(tick,octave))
			return new_melody

		#	do the frechet distance
		#	store the song name and frechet distance stuff
		for song in dict_songs:
			diff = frechet(str_to_arr(song.melody),melody_transpose(str_to_arr(self.melody)),str_to_arr(song.starts))
			title = title_from_path(song.file_path)
			# prints message to update user on progress
			print title + " processed."
			song_diffs.append((title,diff))
		
		# get the top 5 shortest lengths of song in the dictionary ranked by difference
		sorted_diffs = sorted(song_diffs,key=lambda song: song[1])
		return sorted_diffs[:5]

#remove melodia tag from a filename
def remove_tag(name):
	if melodia_tag in name:
		name = name.replace(melodia_tag,"")
	return name

#to get a nice version of the title - minus all the filepath bits
def title_from_path(path):
	return ntpath.basename(remove_tag(path)).split(".")[0]

# turns melody string into array
def str_to_arr(str):
	return json.loads(str)	
