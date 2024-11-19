from models import categoryModel
from .baseRepository import BaseRepository

class CategoryRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(db_session, categoryModel)