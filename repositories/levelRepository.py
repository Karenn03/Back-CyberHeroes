from models import levelModel
from .baseRepository import BaseRepository

class LevelRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(db_session, levelModel)