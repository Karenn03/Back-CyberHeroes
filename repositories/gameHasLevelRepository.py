from models import gameHasLevelModel
from baseRepository import BaseRepository

class GameHasLevelRepository(BaseRepository):
    def get_by_level(self, level_id: int):
        return self.db.query(gameHasLevelModel).filter(gameHasLevelModel.idLevel == level_id).all()