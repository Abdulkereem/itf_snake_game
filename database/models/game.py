from sqlalchemy import *

from config import db, engine




class User(db):
    __tablename__ ="Users"

    id              = Column(Integer,primary_key=True)
    fullname        = Column(String(255))
    username        = Column(String(255),unique=True)
    email           = Column(String(255),unique=True)


# class GameSettings(db):
#     pass

# class GameProfile(db):
#     pass

def migrate():
    db.metadata.create_all(bind=engine)


