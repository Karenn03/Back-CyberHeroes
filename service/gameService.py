from dto.gameDto import GameDTO
from repositories.gameRepository import GameRepository

class GameService:
    def __init__(self, db_session):
        self.game_repository = GameRepository(db_session)

    def get_all_games(self):
        games = self.game_repository.find_all()
        return [GameDTO(game.idGame, game.idUser, game.startDate, game.endDate, game.finalScore) for game in games]

    def get_game_by_id(self, game_id):
        game = self.game_repository.find_by_id(game_id)
        if game:
            return GameDTO(game.idGame, game.idUser, game.startDate, game.endDate, game.finalScore)
        return None

    def create_game(self, game_dto: GameDTO):
        game = self.game_repository.create(game_dto)
        return game

    def update_game(self, game_id, game_dto: GameDTO):
        game = self.game_repository.update(game_id, game_dto)
        return game

    def delete_game(self, game_id):
        self.game_repository.delete(game_id)