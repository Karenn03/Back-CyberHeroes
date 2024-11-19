from models import monsterModel
from baseRepository import BaseRepository

class MonstersRepository(BaseRepository):
    def get_by_level(self, level_id: int):
        return self.db.query(monsterModel).filter(monsterModel.idLevel == level_id).all()