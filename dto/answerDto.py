class AnswerDTO:
    def __init__(self, idAnswer, idQuestion, answer, isCorrect):
        self.idAnswer = idAnswer
        self.idQuestion = idQuestion
        self.answer = answer
        self.isCorrect = isCorrect

    def to_dict(self):
        return {
            "idAnswer": self.idAnswer,
            "idQuestion": self.idQuestion,
            "answer": self.answer,
            "isCorrect": self.isCorrect
        }