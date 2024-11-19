from models import questionModel
from baseRepository import BaseRepository

class QuestionRepository(BaseRepository):
    def find_all(self):
        return self.db.query(questionModel).all()