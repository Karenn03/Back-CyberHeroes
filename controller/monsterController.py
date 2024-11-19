from flask import Blueprint, request, jsonify
from service.monsterService import MonsterService
from dto.monsterDto import MonsterDTO

monsters_bp = Blueprint('monsters', __name__)

monster_service = MonsterService()

@monsters_bp.route('/api/monsters', methods=['GET'])
def get_all_monsters():
    monsters = monster_service.get_all_monsters()
    if monsters:
        return jsonify([monster.to_dict() for monster in monsters]), 200
    return jsonify({'message': 'No monsters found'}), 404

@monsters_bp.route('/api/monsters/<int:monster_id>', methods=['GET'])
def get_monster_by_id(monster_id):
    monster = monster_service.get_monster_by_id(monster_id)
    if monster:
        return jsonify(monster.to_dict()), 200
    return jsonify({'message': 'Monster not found'}), 404

@monsters_bp.route('/api/monsters', methods=['POST'])
def create_monster():
    monster_data = request.get_json()
    monster_dto = MonsterDTO(**monster_data)
    new_monster = monster_service.create_monster(monster_dto)
    return jsonify(new_monster.to_dict()), 201

@monsters_bp.route('/api/monsters/<int:monster_id>', methods=['PUT'])
def update_monster(monster_id):
    monster_data = request.get_json()
    monster_dto = MonsterDTO(**monster_data)
    updated_monster = monster_service.update_monster(monster_id, monster_dto)
    return jsonify(updated_monster.to_dict()), 200

@monsters_bp.route('/api/monsters/<int:monster_id>', methods=['DELETE'])
def delete_monster(monster_id):
    monster_service.delete_monster(monster_id)
    return jsonify({'message': 'Monster deleted successfully'}), 200