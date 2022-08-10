from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base

db  = declarative_base()

class User(db):
    __tabelname__ = "user_account"

    id =  Column(Integer,primary_key=True)
    fullname = Column(String(255))
    gender  = Column(String(30))