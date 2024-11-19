from flask import Blueprint, request, jsonify
from service.levelService import LevelService
from dto.levelDto import LevelDTO
from app import db

level_bp = Blueprint('level', __name__)

level_service = LevelService(db.session)

@level_bp.route('/api/levels', methods=['GET'])
def get_all_levels():
    levels = level_service.get_all_levels()
    if levels:
        return jsonify([level.to_dict() for level in levels]), 200
    return jsonify({'message': 'No levels found'}), 404

@level_bp.route('/api/levels/<id>', methods=['GET'])
def get_level_by_id(level_id):
    level = level_service.get_level_by_id(level_id)
    if level:
        return jsonify(level.to_dict()), 200
    return jsonify({'message': 'Level not found'}), 404

@level_bp.route('/api/levels', methods=['POST'])
def create_level():
    level_data = request.get_json()
    level_dto = LevelDTO(**level_data)
    new_level = level_service.create_level(level_dto)
    return jsonify(new_level.to_dict()), 201

@level_bp.route('/api/levels/<id>', methods=['PUT'])
def update_level(level_id):
    level_data = request.get_json()
    level_dto = LevelDTO(**level_data)
    updated_level = level_service.update_level(level_id, level_dto)
    return jsonify(updated_level.to_dict()), 200

@level_bp.route('/api/levels/<id>', methods=['DELETE'])
def delete_level(level_id):
    level_service.delete_level(level_id)
    return jsonify({'message': 'Level deleted successfully'}), 200