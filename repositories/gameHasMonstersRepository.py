from models import gameHasMonstersModel
from .baseRepository import BaseRepository

class GameHasMonstersRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(db_session, gameHasMonstersModel)

    def find_all(self):
        return self.db.query(gameHasMonstersModel).all()
    
    def get_by_game(self, game_id: int):
        return self.db.query(gameHasMonstersModel).filter(gameHasMonstersModel.idGame == game_id).all()