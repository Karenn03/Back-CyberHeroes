class CategoryDTO:
    def __init__(self, idCategory, idMonsters, category):
        self.idCategory = idCategory
        self.idMonsters = idMonsters
        self.category = category

    def to_dict(self):
        return {
            "idCategory": self.idCategory,
            "idMonsters": self.idMonsters,
            "category": self.category
        }