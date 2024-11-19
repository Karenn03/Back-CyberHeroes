from flask import Blueprint, request, jsonify
from service.questionService import QuestionService
from dto.questionDto import QuestionDTO
from app import db

questions_bp = Blueprint('questions', __name__)

question_service = QuestionService(db.session)

@questions_bp.route('/api/questions', methods=['GET'])
def get_all_questions():
    questions = question_service.get_all_questions()
    if questions:
        return jsonify([question.to_dict() for question in questions]), 200
    return jsonify({'message': 'No questions found'}), 404

@questions_bp.route('/api/questions/<int:question_id>', methods=['GET'])
def get_question_by_id(question_id):
    question = question_service.get_question_by_id(question_id)
    if question:
        return jsonify(question.to_dict()), 200
    return jsonify({'message': 'Question not found'}), 404

@questions_bp.route('/api/questions', methods=['POST'])
def create_question():
    try:
        question_data = request.get_json()
        question_dto = QuestionDTO(**question_data)
        new_question = question_service.create_question(question_dto)
        return jsonify(new_question.to_dict()), 201
    except Exception as e:
        return jsonify({'message': f"Error creating question: {str(e)}"}), 500

@questions_bp.route('/api/questions/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    question_data = request.get_json()
    question_dto = QuestionDTO(**question_data)
    updated_question = question_service.update_question(question_id, question_dto)
    if updated_question:
        return jsonify(updated_question.to_dict()), 200
    return jsonify({'message': 'Question not found'}), 404

@questions_bp.route('/api/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    try:
        question_service.delete_question(question_id)
        return jsonify({'message': 'Question deleted successfully'}), 200
    except Exception as e:
        return jsonify({'message': f"Error deleting question: {str(e)}"}), 500