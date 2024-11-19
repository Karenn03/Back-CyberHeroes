from models import categoryModel
from dto.categoryDto import CategoryDTO
from repositories.categoryRepository import CategoryRepository

class CategoryService:
    def __init__(self, db_session):
        self.category_repository = CategoryRepository(db_session)

    def get_all_categories(self):
        categories = self.category_repository.get_all()
        return [CategoryDTO(category.idCategory, category.idMonsters, category.category) for category in categories]

    def get_category_by_id(self, category_id):
        category = self.category_repository.get_by_id(category_id)
        if category:
            return CategoryDTO(category.idCategory, category.idMonsters, category.category)
        return None

    def create_category(self, category_dto: CategoryDTO):
        new_category = categoryModel(
            idMonsters=category_dto.idMonsters,
            category=category_dto.category
        )
        return self.category_repository.add(new_category)

    def update_category(self, category_id, category_dto: CategoryDTO):
        category = self.category_repository.get_by_id(category_id)
        if category:
            category.idMonsters = category_dto.idMonsters
            category.category = category_dto.category
            return self.category_repository.update(category)
        return None

    def delete_category(self, category_id):
        self.category_repository.delete(category_id)