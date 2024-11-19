from flask import Blueprint, request, jsonify
from service.gameService import GameService
from dto.gameDto import GameDTO

game_bp = Blueprint('game', __name__)

game_service = GameService()

@game_bp.route('/api/games', methods=['GET'])
def get_all_games():
    games = game_service.get_all_games()
    if games:
        return jsonify([game.to_dict() for game in games]), 200
    return jsonify({'message': 'No games found'}), 404

@game_bp.route('/api/games/<id>', methods=['GET'])
def get_game_by_id(game_id):
    game = game_service.get_game_by_id(game_id)
    if game:
        return jsonify(game.to_dict()), 200
    return jsonify({'message': 'Game not found'}), 404

@game_bp.route('/api/games', methods=['POST'])
def create_game():
    game_data = request.get_json()
    game_dto = GameDTO(**game_data)
    new_game = game_service.create_game(game_dto)
    return jsonify(new_game.to_dict()), 201

@game_bp.route('/api/games/<id>', methods=['PUT'])
def update_game(game_id):
    game_data = request.get_json()
    game_dto = GameDTO(**game_data)
    updated_game = game_service.update_game(game_id, game_dto)
    return jsonify(updated_game.to_dict()), 200

@game_bp.route('/api/games/<id>', methods=['DELETE'])
def delete_game(game_id):
    game_service.delete_game(game_id)
    return jsonify({'message': 'Game deleted successfully'}), 200