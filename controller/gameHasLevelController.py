from flask import Blueprint, request, jsonify
from service.gameHasLevelService import GameHasLevelService

gameHasLevel_bp = Blueprint('gameHasLevel', __name__)

game_has_level_service = GameHasLevelService()

@gameHasLevel_bp.route('/api/gameHasLevel', methods=['GET'])
def get_all_game_has_levels():
    game_has_levels = game_has_level_service.get_all_game_has_levels()
    if game_has_levels:
        return jsonify([ghl.to_dict() for ghl in game_has_levels]), 200
    return jsonify({'message': 'No game-level associations found'}), 404

@gameHasLevel_bp.route('/api/gameHasLevel', methods=['POST'])
def create_game_has_level():
    data = request.get_json()
    new_relation = game_has_level_service.create_game_has_level(data['game_id'], data['level_id'])
    return jsonify(new_relation.to_dict()), 201

@gameHasLevel_bp.route('/api/gameHasLevel/<int:gameHasLevel_id>', methods=['DELETE'])
def delete_game_has_level(game_id, level_id):
    game_has_level_service.delete_game_has_level(game_id, level_id)
    return jsonify({'message': 'Relation deleted successfully'}), 200
