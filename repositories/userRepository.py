from models import userModel
from baseRepository import BaseRepository

class UserRepository(BaseRepository):
    def find_all(self):
        return self.db.query(userModel).all()

    def get_by_id_card(self, id_card: int):
        return self.db.query(userModel).filter(userModel.idCard == id_card).first()

    def get_by_email(self, email: str):
        return self.db.query(userModel).filter(userModel.email == email).first()