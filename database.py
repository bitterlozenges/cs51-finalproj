#from sqlalchemy import Table, Column, Integer, String, Text
#from sqlalchemy import create_engine, MetaData
from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker, mapper

engine = create_engine('sqlite:///finalproj.db',convert_unicode=True)

engine.echo = False

metadata = MetaData(engine)

db_session = scoped_session(sessionmaker(autocommit=False, 
											autoflush=False, bind=engine))


def init_db():
    metadata.create_all()