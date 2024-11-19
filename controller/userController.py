from flask import Blueprint, request, jsonify
from service.userService import UserService
from dto.userDto import UserDTO

users_bp = Blueprint('users', __name__)

user_service = UserService()

@users_bp.route('/api/users', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    if users:
        users_list = [user.to_dict() for user in users]
        return jsonify(users_list), 200
    return jsonify({'message': 'No users found'}), 404

@users_bp.route('/api/users/<id>', methods=['GET'])
def get_user_by_id(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'message': 'User not found'}), 404

@users_bp.route('/api/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_dto = UserDTO(**user_data)
    new_user = user_service.create_user(user_dto)
    return jsonify(new_user.to_dict()), 201

@users_bp.route('/api/users/<id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    user_dto = UserDTO(**user_data)
    updated_user = user_service.update_user(user_id, user_dto)
    return jsonify(updated_user.to_dict()), 200

@users_bp.route('/users/<id>', methods=['DELETE'])
def delete_user(user_id):
    user_service.delete_user(user_id)
    return jsonify({'message': 'User deleted successfully'}), 200