from models import gameHasLevelModel
from .baseRepository import BaseRepository

class GameHasLevelRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(db_session, gameHasLevelModel)

    def find_all(self):
        return self.db.query(gameHasLevelModel).all()
    
    def get_by_level(self, level_id: int):
        return self.db.query(gameHasLevelModel).filter(gameHasLevelModel.idLevel == level_id).all()