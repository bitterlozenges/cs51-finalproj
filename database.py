#from sqlalchemy import Table, Column, Integer, String, Text
#from sqlalchemy import create_engine, MetaData
from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker
#from models import Song

engine = create_engine('sqlite:///finalproj.db',convert_unicode=True)

engine.echo = False

metadata = MetaData()

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


"""
songs = Table('songs', metadata,
    Column('id', Integer, primary_key=True),
    Column('file_path', String(50), unique=True),
    Column('melody', Text),
    Column('diffs', Text),
    Column('starts', Text)
)
"""
#mapper(Song, songs)

def init_db():
    metadata.create_all(bind=engine)

