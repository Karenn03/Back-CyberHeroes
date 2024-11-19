from dto.gameHasMonstersDto import GameHasMonstersDTO
from repositories.gameHasMonstersRepository import GameHasMonstersRepository

class GameHasMonstersService:
    def __init__(self, db_session):
        self.game_has_monsters_repository = GameHasMonstersRepository(db_session)

    def get_all_game_has_monsters(self):
        game_has_monsters = self.game_has_monsters_repository.find_all()
        return [
            GameHasMonstersDTO(
                game.idGame, 
                game.idMonsters
            ) for game in game_has_monsters
        ]

    def get_game_has_monsters_by_id(self, game_has_monsters_id):
        game_has_monsters = self.game_has_monsters_repository.find_by_id(game_has_monsters_id)
        if game_has_monsters:
            return GameHasMonstersDTO(
                game_has_monsters.idGameHasMonsters,
                game_has_monsters.idGame,
                game_has_monsters.idUser,
                game_has_monsters.idMonsters,
                game_has_monsters.idLevel
            )
        return None

    def create_game_has_monsters(self, game_has_monsters_dto: GameHasMonstersDTO):
        game_has_monsters = self.game_has_monsters_repository.create(game_has_monsters_dto)
        return game_has_monsters

    def update_game_has_monsters(self, game_has_monsters_id, game_has_monsters_dto: GameHasMonstersDTO):
        game_has_monsters = self.game_has_monsters_repository.update(game_has_monsters_id, game_has_monsters_dto)
        return game_has_monsters

    def delete_game_has_monsters(self, game_has_monsters_id):
        self.game_has_monsters_repository.delete(game_has_monsters_id)