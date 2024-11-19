from dto.levelDto import LevelDTO
from repositories.levelRepository import LevelRepository

class LevelService:
    def __init__(self, db_session):
        self.level_repository = LevelRepository(db_session)

    def get_all_levels(self):
        levels = self.level_repository.get_all()
        return [LevelDTO(level.idLevel, level.difficulty) for level in levels]

    def get_level_by_id(self, level_id):
        level = self.level_repository.get_by_id(level_id)
        if level:
            return LevelDTO(level.idLevel, level.difficulty)
        return None

    def create_level(self, level_dto: LevelDTO):
        level = self.level_repository.create(level_dto)
        return level

    def update_level(self, level_id, level_dto: LevelDTO):
        level = self.level_repository.update(level_id, level_dto)
        return level

    def delete_level(self, level_id):
        self.level_repository.delete(level_id)