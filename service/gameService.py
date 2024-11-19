from dto.gameDto import GameDTO
from repositories.gameRepository import GameRepository

class GameService:
    def __init__(self, db_session):
        self.game_repository = GameRepository(db_session)

    def get_all_games(self):
        games = self.game_repository.get_all()
        return [GameDTO(game.idGame, game.idUser, game.startDate, game.endDate, game.finalScore) for game in games]

    def get_game_by_id(self, game_id):
        game = self.game_repository.get_by_id(game_id)
        if game:
            return GameDTO(game.idGame, game.idUser, game.startDate, game.endDate, game.finalScore)
        return None

    def create_game(self, game_dto: GameDTO):
        self.validate_dates(game_dto.startDate, game_dto.endDate)
        game = self.game_repository.create(game_dto)
        return GameDTO(game.idGame, game.idUser, game.startDate, game.endDate, game.finalScore)

    def update_game(self, game_id, game_dto: GameDTO):
        existing_game = self.game_repository.get_by_id(game_id)
        if not existing_game:
            raise ValueError(f"Game with ID {game_id} does not exist.")
        self.validate_dates(game_dto.startDate, game_dto.endDate)
        updated_game = self.game_repository.update(game_id, game_dto)
        return GameDTO(updated_game.idGame, updated_game.idUser, updated_game.startDate, updated_game.endDate, updated_game.finalScore)

    def delete_game(self, game_id):
        existing_game = self.game_repository.get_by_id(game_id)
        if not existing_game:
            raise ValueError(f"Game with ID {game_id} does not exist.")
        self.game_repository.delete(game_id)