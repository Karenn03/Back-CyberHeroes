from flask import Blueprint, request, jsonify
from service.categoryService import CategoryService
from dto.categoryDto import CategoryDTO
from app import db

categories_bp = Blueprint('categories', __name__)

category_service = CategoryService(db.session)

@categories_bp.route('/api/categories', methods=['GET'])
def get_all_categories():
    categories = category_service.get_all_categories()
    if categories:
        return jsonify([category.to_dict() for category in categories]), 200
    return jsonify({'message': 'No categories found'}), 404

@categories_bp.route('/api/categories/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    category = category_service.get_category_by_id(category_id)
    if category:
        return jsonify(category.to_dict()), 200
    return jsonify({'message': 'Category not found'}), 404

@categories_bp.route('/api/categories', methods=['POST'])
def create_category():
    try:
        category_data = request.get_json()
        category_dto = CategoryDTO(**category_data)
        new_category = category_service.create_category(category_dto)
        return jsonify(new_category.to_dict()), 201
    except Exception as e:
        return jsonify({'message': f"Error creating category: {str(e)}"}), 500

@categories_bp.route('/api/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category_data = request.get_json()
    category_dto = CategoryDTO(**category_data)
    updated_category = category_service.update_category(category_id, category_dto)
    if updated_category:
        return jsonify(updated_category.to_dict()), 200
    return jsonify({'message': 'Category not found'}), 404

@categories_bp.route('/api/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    try:
        category_service.delete_category(category_id)
        return jsonify({'message': 'Category deleted successfully'}), 200
    except Exception as e:
        return jsonify({'message': f"Error deleting category: {str(e)}"}), 500