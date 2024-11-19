from dto.monsterDto import MonsterDTO
from repositories.monsterRepository import MonsterRepository

class MonsterService:
    def __init__(self, db_session):
        self.monster_repository = MonsterRepository(db_session)

    def get_all_monsters(self):
        monsters = self.monster_repository.find_all()
        return [MonsterDTO(monster.idMonsters, monster.idLevel, monster.name, monster.description) for monster in monsters]

    def get_monster_by_id(self, monster_id):
        monster = self.monster_repository.find_by_id(monster_id)
        if monster:
            return MonsterDTO(monster.idMonsters, monster.idLevel, monster.name, monster.description)
        return None

    def create_monster(self, monster_dto: MonsterDTO):
        monster = self.monster_repository.create(monster_dto)
        return monster

    def update_monster(self, monster_id, monster_dto: MonsterDTO):
        monster = self.monster_repository.update(monster_id, monster_dto)
        return monster

    def delete_monster(self, monster_id):
        self.monster_repository.delete(monster_id)