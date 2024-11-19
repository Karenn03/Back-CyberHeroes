from models import gameHasMonstersModel
from baseRepository import BaseRepository

class GameHasMonstersRepository(BaseRepository):
    def find_all(self):
        return self.db.query(gameHasMonstersModel).all()
    
    def get_by_game(self, game_id: int):
        return self.db.query(gameHasMonstersModel).filter(gameHasMonstersModel.idGame == game_id).all()