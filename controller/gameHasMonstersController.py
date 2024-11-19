from flask import Blueprint, request, jsonify
from service.gameHasMonstersService import GameHasMonstersService

gameHasMonsters_bp = Blueprint('gameHasMonsters', __name__)

game_has_monsters_service = GameHasMonstersService()

@gameHasMonsters_bp.route('/api/gameHasMonsters', methods=['GET'])
def get_all_game_has_monsters():
    game_has_monsters = game_has_monsters_service.get_all_game_has_monsters()
    if game_has_monsters:
        return jsonify([ghm.to_dict() for ghm in game_has_monsters]), 200
    return jsonify({'message': 'No game-monsters associations found'}), 404

@gameHasMonsters_bp.route('/api/gameHasMonsters', methods=['POST'])
def create_game_has_monster():
    data = request.get_json()
    new_relation = game_has_monsters_service.create_game_has_monster(data['game_id'], data['monster_id'])
    return jsonify(new_relation.to_dict()), 201

@gameHasMonsters_bp.route('/api/gameHasMonsters/<int:gameHasMonsters_id>', methods=['DELETE'])
def delete_game_has_monster(game_id, monster_id):
    game_has_monsters_service.delete_game_has_monster(game_id, monster_id)
    return jsonify({'message': 'Relation deleted successfully'}), 200