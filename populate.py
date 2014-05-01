from sqlalchemy import *
from analyze import *
from models import Song #get database, songs table, and Song class
from database import db_session
#from os.path import *

#the path for the file containing the list of files to be put in the array
folder_path = "file_list.txt"

#method for inserting a single song into our db given the file_path
def insert_song_db(file):
	# if the file exists
	if true: #os.path.isfile(fname):
		song = Song(file)
		#add the song to the current session
		db_session.add(song)
		return
	# if there is no file with that name
	else: 
		print 'No file with name ' + file

#method for inserting every filepath in a file into our db
def insert_list_db(file):
	f = open(file, 'r')
	for line in f:
		insert_song_db(line.rstrip('\n'))
	#after adding each song to the current session, commit all changes
	db_session.commit()
	f.close()
	return

