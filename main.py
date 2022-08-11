from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine 

engine = create_engine('sqlite:///test.db')

db  = declarative_base()

class User(db):
    __tabelname__ = "user_account"

    id =  Column(Integer,primary_key=True)
    fullname = Column(String(255))
    gender  = Column(String(30))