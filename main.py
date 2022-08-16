from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine 

engine = create_engine('sqlite:///test.db')

db  = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()

class User(db):
    __tablename__ = "user_account"

    id =  Column(Integer,primary_key=True)
    fullname = Column(String(255))
    gender  = Column(String(30))


user1 = User(fullname='Abdul Ironside',gender='male')
session.add(user1)
session.commit()
#db.metadata.create_all(engine)
