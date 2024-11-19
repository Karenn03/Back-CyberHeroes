from models import userModel
from .baseRepository import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(db_session, userModel)

    def get_by_id_card(self, id_card: int):
        try:
            return self.db.query(userModel).filter(userModel.idCard == id_card).first()
        except Exception as e:
            raise Exception(f"Error retrieving user by ID card: {e}")

    def get_by_email(self, email: str):
        try:
            return self.db.query(userModel).filter(userModel.email == email).first()
        except Exception as e:
            raise Exception(f"Error retrieving user by email: {e}")