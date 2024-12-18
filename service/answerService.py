from models import answerModel
from dto.answerDto import AnswerDTO
from repositories.answerRepository import AnswerRepository

class AnswerService:
    def __init__(self, db_session):
        self.answer_repository = AnswerRepository(db_session)

    def get_all_answers(self):
        answers = self.answer_repository.get_all()
        return [AnswerDTO(answer.idAnswer, answer.idQuestion, answer.correct, answer.content) for answer in answers]

    def get_answer_by_id(self, answer_id):
        answer = self.answer_repository.get_by_id(answer_id)
        if answer:
            return AnswerDTO(answer.idAnswer, answer.idQuestion, answer.answer, answer.isCorrect)
        return None

    def create_answer(self, answer_dto: AnswerDTO):
        new_answer = answerModel(
            idAnswer=answer_dto.idAnswer,
            idQuestion=answer_dto.idQuestion,
            answer=answer_dto.answer,
            isCorrect=answer_dto.isCorrect
        )
        return self.answer_repository.add(new_answer)

    def update_answer(self, answer_id, answer_dto: AnswerDTO):
        answer = self.answer_repository.find_by_id(answer_id)
        if answer:
            answer.idQuestion = answer_dto.idQuestion
            answer.answer = answer_dto.answer
            answer.isCorrect = answer_dto.isCorrect
            return self.answer_repository.update(answer)
        return None

    def delete_answer(self, answer_id):
        self.answer_repository.delete(answer_id)