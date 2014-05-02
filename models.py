from sqlalchemy import Table, Column, Integer, String, Text
from sqlalchemy.orm import mapper
import json
from database import db_session, metadata
from analyze import *
#for the split function
import re
from distance import frechet

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

	def str_to_arr(self):
		tmp = json.loads(self.melody)	
		self.melody = tmp



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
    Column('file_path', String(50), unique=True),
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
	# returns top 10 matches
	def get_matches(self):
		
		# gets dictionary of songs
		dict_songs = Song.query.all()
		song_diffs = []

		# turn melody "strings" of each song object into an array 
		for song in dict_songs:
			song.str_to_arr

		#	do the frechet distance
		#	store the song name and frechet distance stuff
		for song in dict_songs:
			diff = frechet(song.melody,str_to_arr(self.melody),song.starts)
			title = title_from_path(song.file_path)
			song_diffs.append((title,diff))
		
		# get the top 10 shortest lengths of song in the dictionary in ranked order
		def getKey(item):
			item[1]

		sorted_diffs = sorted(song_diffs, key = getKey)

		return sorted_diffs[:10]

#to get a nice version of the title - minus all the filepath bits
def title_from_path(str):
	arr = file.split()
	if len(arr) > 2:
		title = re.split('[./]', file)[len(arr)-2]
	else:
		title = file
	return title

'''
# object hook for getting a song object from a json string
def as_song(dic):
	file_path = dic['file_path']
	melody = dic['melody']
	starts = dic['starts']
	return Song(file_path,melody,starts)

# returns a song given a json string
def to_song(str):
	return json.loads(str,object_hook=as_song)
'''
