from models import gameModel
from .baseRepository import BaseRepository

class GameRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(db_session, gameModel)

    def get_by_user(self, user_id: int):
        return self.db.query(gameModel).filter(gameModel.idUser == user_id).all()