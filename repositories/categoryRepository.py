from models import categoryModel
from baseRepository import BaseRepository

class CategoryRepository(BaseRepository):
    def find_all(self):
        return self.db.query(categoryModel).all()