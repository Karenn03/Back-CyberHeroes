from models import monsterModel
from dto.monsterDto import MonsterDTO
from repositories.monsterRepository import MonstersRepository

class MonsterService:
    def __init__(self, db_session):
        self.monster_repository = MonstersRepository(db_session)

    def get_all_monsters(self):
        monsters = self.monster_repository.get_all()
        return [MonsterDTO(monster.idMonsters, monster.idLevel, monster.name, monster.description) for monster in monsters]

    def get_monster_by_id(self, monster_id):
        monster = self.monster_repository.get_by_id(monster_id)
        if monster:
            return MonsterDTO(monster.idMonsters, monster.idLevel, monster.name, monster.description)
        return None

    def create_monster(self, monster_dto: MonsterDTO):
        new_monster = monsterModel(
            idLevel=monster_dto.idLevel,
            name=monster_dto.name,
            description=monster_dto.description
        )
        return self.monster_repository.add(new_monster)

    def update_monster(self, monster_id, monster_dto: MonsterDTO):
        monster = self.monster_repository.get_by_id(monster_id)
        if monster:
            monster.idLevel = monster_dto.idLevel
            monster.name = monster_dto.name
            monster.description = monster_dto.description
            return self.monster_repository.update(monster)
        return None

    def delete_monster(self, monster_id):
        self.monster_repository.delete(monster_id)