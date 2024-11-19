from dto.gameHasLevelDto import GameHasLevelDTO
from repositories.gameHasLevelRepository import GameHasLevelRepository

class GameHasLevelService:
    def __init__(self, db_session):
        self.game_has_level_repository = GameHasLevelRepository(db_session)

    def get_all_game_has_levels(self):
        game_has_levels = self.game_has_level_repository.find_all()
        return [
            GameHasLevelDTO(
                game.idGame, 
                game.idLevel
            ) for game in game_has_levels
        ]

    def get_game_has_level_by_id(self, game_has_level_id):
        game_has_level = self.game_has_level_repository.find_by_id(game_has_level_id)
        if game_has_level:
            return GameHasLevelDTO(game_has_level.idGameHasLevel, game_has_level.idGame, game_has_level.idUser, game_has_level.idLevel)
        return None

    def create_game_has_level(self, game_has_level_dto: GameHasLevelDTO):
        game_has_level = self.game_has_level_repository.create(game_has_level_dto)
        return game_has_level

    def update_game_has_level(self, game_has_level_id, game_has_level_dto: GameHasLevelDTO):
        game_has_level = self.game_has_level_repository.update(game_has_level_id, game_has_level_dto)
        return game_has_level

    def delete_game_has_level(self, game_has_level_id):
        self.game_has_level_repository.delete(game_has_level_id)