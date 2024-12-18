from flask import Blueprint, request, jsonify
from service.answerService import AnswerService
from dto.answerDto import AnswerDTO
from app import db

answers_bp = Blueprint('answers', __name__)

answer_service = AnswerService(db.session)

@answers_bp.route('/api/answers', methods=['GET'])
def get_all_answers():
    answers = answer_service.get_all_answers()
    if answers:
        return jsonify([answer.to_dict() for answer in answers]), 200
    return jsonify({'message': 'No answers found'}), 404

@answers_bp.route('/api/answers/<int:answer_id>', methods=['GET'])
def get_answer_by_id(answer_id):
    answer = answer_service.get_answer_by_id(answer_id)
    if answer:
        return jsonify(answer.to_dict()), 200
    return jsonify({'message': 'Answer not found'}), 404

@answers_bp.route('/api/answers', methods=['POST'])
def create_answer():
    try:
        answer_data = request.get_json()
        answer_dto = AnswerDTO(**answer_data)
        new_answer = answer_service.create_answer(answer_dto)
        return jsonify(new_answer.to_dict()), 201
    except Exception as e:
        return jsonify({'message': f"Error creating answer: {str(e)}"}), 500

@answers_bp.route('/api/answers/<int:answer_id>', methods=['PUT'])
def update_answer(answer_id):
    answer_data = request.get_json()
    answer_dto = AnswerDTO(**answer_data)
    updated_answer = answer_service.update_answer(answer_id, answer_dto)
    if updated_answer:
        return jsonify(updated_answer.to_dict()), 200
    return jsonify({'message': 'Answer not found'}), 404

@answers_bp.route('/api/answers/<int:answer_id>', methods=['DELETE'])
def delete_answer(answer_id):
    try:
        answer_service.delete_answer(answer_id)
        return jsonify({'message': 'Answer deleted successfully'}), 200
    except Exception as e:
        return jsonify({'message': f"Error deleting answer: {str(e)}"}), 500