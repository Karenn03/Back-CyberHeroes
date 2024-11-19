from models import answerModel
from baseRepository import BaseRepository

class AnswerRepository(BaseRepository):
    def find_all(self):
        return self.db.query(answerModel).all()
    
    def get_correct_answers(self, question_id: int):
        return self.db.query(answerModel).filter(answerModel.idQuestion == question_id, answerModel.isCorrect == True).all()