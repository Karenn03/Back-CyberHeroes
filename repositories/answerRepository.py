from models import answerModel
from .baseRepository import BaseRepository

class AnswerRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(db_session, answerModel)

    def get_correct_answers(self, question_id: int):
        return self.db.query(answerModel).filter(answerModel.idQuestion == question_id, answerModel.isCorrect == True).all()