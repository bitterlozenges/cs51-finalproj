from sqlalchemy import *
from analyze import *
from models import Song #get database, songs table, and Song class
from database import db_session, init_db
import os
"""
This script deletes any old instances of the database, creates a new one,
then repopulates it with the files in folder_path
"""

#the path for the file containing the list of files to be put in the array
folder_path = "file_list.txt"

#method for inserting a single song into our db given the file_path
def insert_song_db(file):
	# if the file exists
	if os.path.isfile(file):
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
		insert_song_db(line.strip('\t\n\r'))
	#after adding each song to the current session, commit all changes
	db_session.commit()
	f.close()
	return


#remove the old databse file
if os.path.isfile("finalproj.db"):
	os.remove("finalproj.db")
#initialize the database
init_db()
#populate it with our things
insert_list_db(folder_path)