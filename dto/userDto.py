class UserDTO:
    def __init__(self, idUser, idCard, names, surnames, email, password, score):
        self.idUser = idUser
        self.idCard = idCard
        self.names = names
        self.surnames = surnames
        self.email = email
        self.password = password
        self.score = score

    def to_dict(self):
        return {
            "idUser": self.idUser,
            "idCard": self.idCard,
            "names": self.names,
            "surnames": self.surnames,
            "email": self.email,
            "score": self.score
        }