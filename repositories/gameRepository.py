from models import gameModel
from baseRepository import BaseRepository

class GameRepository(BaseRepository):
    def get_by_user(self, user_id: int):
        return self.db.query(gameModel).filter(gameModel.idUser == user_id).all()