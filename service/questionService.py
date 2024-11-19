from models import questionModel
from dto.questionDto import QuestionDTO
from repositories.questionRepository import QuestionRepository

class QuestionService:
    def __init__(self, db_session):
        self.question_repository = QuestionRepository(db_session)

    def get_all_questions(self):
        questions = self.question_repository.get_all()
        return [QuestionDTO(question.idQuestion, question.idCategory, question.content) for question in questions]

    def get_question_by_id(self, question_id):
        question = self.question_repository.get_by_id(question_id)
        if question:
            return QuestionDTO(question.idQuestion, question.idCategory, question.content)
        return None

    def create_question(self, question_dto: QuestionDTO):
        new_question = questionModel(
            idCategory=question_dto.idCategory,
            content=question_dto.content
        )
        return self.question_repository.add(new_question)

    def update_question(self, question_id, question_dto: QuestionDTO):
        question = self.question_repository.get_by_id(question_id)
        if question:
            question.idCategory = question_dto.idCategory
            question.content = question_dto.content
            return self.question_repository.update(question)
        return None

    def delete_question(self, question_id):
        self.question_repository.delete(question_id)