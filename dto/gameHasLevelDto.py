class GameHasLevelDTO:
    def __init__(self, idGameHasLevel, idGame, idUser, idLevel):
        self.idGameHasLevel = idGameHasLevel
        self.idGame = idGame
        self.idUser = idUser
        self.idLevel = idLevel

    def to_dict(self):
        return {
            "idGameHasLevel": self.idGameHasLevel,
            "idGame": self.idGame,
            "idUser": self.idUser,
            "idLevel": self.idLevel
        }