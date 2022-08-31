from .game import User, SessionHandler
from database.config import db , session


class QueryDB:
    def __init__(self) -> None:
        pass 

    @staticmethod    
    def get_user(username:str):
        return session.query(User).filter_by(username=username).first()

    @staticmethod
    def current_user():
        return session.query(SessionHandler).first()



