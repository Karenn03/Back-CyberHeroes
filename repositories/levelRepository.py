from models import levelModel
from baseRepository import BaseRepository

class LevelRepository(BaseRepository):
    def find_all(self):
        return self.db.query(levelModel).all()