from models import questionModel
from .baseRepository import BaseRepository

class QuestionRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(db_session, questionModel)