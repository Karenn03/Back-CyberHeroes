class QuestionDTO:
    def __init__(self, idQuestion, idCategory, content):
        self.idQuestion = idQuestion
        self.idCategory = idCategory
        self.content = content

    def to_dict(self):
        return {
            "idQuestion": self.idQuestion,
            "idCategory": self.idCategory,
            "content": self.content
        }