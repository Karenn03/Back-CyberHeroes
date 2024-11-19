class LevelDTO:
    def __init__(self, idLevel, difficulty):
        self.idLevel = idLevel
        self.difficulty = difficulty

    def to_dict(self):
        return {
            "idLevel": self.idLevel,
            "difficulty": self.difficulty
        }