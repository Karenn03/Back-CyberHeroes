class GameDTO:
    def __init__(self, idGame, idUser, startDate, endDate, finalScore):
        self.idGame = idGame
        self.idUser = idUser
        self.startDate = startDate
        self.endDate = endDate
        self.finalScore = finalScore

    def to_dict(self):
        return {
            "idGame": self.idGame,
            "idUser": self.idUser,
            "startDate": self.startDate,
            "endDate": self.endDate,
            "finalScore": self.finalScore
        }