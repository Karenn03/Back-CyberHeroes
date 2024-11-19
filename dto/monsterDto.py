class MonsterDTO:
    def __init__(self, idMonsters, idLevel, name, description):
        self.idMonsters = idMonsters
        self.idLevel = idLevel
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            "idMonsters": self.idMonsters,
            "idLevel": self.idLevel,
            "name": self.name,
            "description": self.description
        }