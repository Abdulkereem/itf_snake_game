from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import sqlite3

sqlite3.connect('test.db')

engine = create_engine('sqlite:///test.db')
db = declarative_base()
session = sessionmaker(bind=engine)


