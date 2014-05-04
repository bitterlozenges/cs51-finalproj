from sqlalchemy import *
from analyze import *
from models import Song #get database, songs table, and Song class
from database import db_session, init_db
from process import *
import os
import sys

"""
This script deletes any old instances of the database, creates a new one,
then repopulates it with the files in song_csv_path, our database of song .csv files
"""

#the path for the directory containing songs to be added to our db
folder_path = str(sys.argv[1])

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

# method for inserting every filepath in a directory into our db
def insert_directory_db(directory):
	filelist = os.listdir(directory)
	for f in filelist:
		# if the file is not a .csv, exclude
		if not ".csv" in f:
			continue
		# adjoin the original directory to the filepath
		path = directory + f
		insert_song_db(path.strip('\t\n\r'))
	db_session.commit()
	return

# remove the old database file
if os.path.isfile("finalproj.db"):
	os.remove("finalproj.db")

# initialize the database
init_db()

# populate 

# first, process each audio file into a .csv
process(folder_path, False)

# add each .csv to our db
# because the .csv files in song_csv_path are not deleted, 
# old .csv files will be kept in our database each time this script is called
insert_directory_db(song_csv_path)
