from dto.questionDto import QuestionDTO
from repositories.questionRepository import QuestionRepository

class QuestionService:
    def __init__(self, db_session):
        self.question_repository = QuestionRepository(db_session)

    def get_all_questions(self):
        questions = self.question_repository.find_all()
        return [QuestionDTO(question.idQuestion, question.idCategory, question.content) for question in questions]

    def get_question_by_id(self, question_id):
        question = self.question_repository.find_by_id(question_id)
        if question:
            return QuestionDTO(question.idQuestion, question.idCategory, question.content)
        return None

    def create_question(self, question_dto: QuestionDTO):
        question = self.question_repository.create(question_dto)
        return question

    def update_question(self, question_id, question_dto: QuestionDTO):
        question = self.question_repository.update(question_id, question_dto)
        return question

    def delete_question(self, question_id):
        self.question_repository.delete(question_id)