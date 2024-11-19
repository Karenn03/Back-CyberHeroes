class GameHasMonstersDTO:
    def __init__(self, idGameHasMonsters, idGame, idUser, idMonsters, idLevel):
        self.idGameHasMonsters = idGameHasMonsters
        self.idGame = idGame
        self.idUser = idUser
        self.idMonsters = idMonsters
        self.idLevel = idLevel

    def to_dict(self):
        return {
            "idGameHasMonsters": self.idGameHasMonsters,
            "idGame": self.idGame,
            "idUser": self.idUser,
            "idMonsters": self.idMonsters,
            "idLevel": self.idLevel
        }