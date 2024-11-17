from flask import Blueprint, request, jsonify
from psycopg2 import connect, extras

questions_bp = Blueprint('questions', __name__)

host = 'localhost'
port = 5432
dbname = 'DBCyberTest'
user = 'postgres'
password = 'KM1013599968'

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn

@questions_bp.get('/api/questions')
def get_questions():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM questions')
    questions = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(questions)

@questions_bp.post('/api/questions')
def create_question():
    new_question = request.get_json()
    idCategory = new_question['idCategory']
    content = new_question['content']

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO questions (idCategory, content) VALUES (%s, %s) RETURNING * ',
                (idCategory, content))
    
    new_created_question = cur.fetchone()
    print(new_created_question)
    conn.commit()
    
    cur.close()
    conn.close()

    return jsonify(new_created_question)

@questions_bp.delete('/api/questions/<id>')
def delete_question(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('DELETE FROM questions WHERE idQuestion = %s RETURNING * ', (id, ))
    question = cur.fetchone()
    
    conn.commit()
    
    conn.close()
    cur.close()
    
    if question is None:
        return jsonify({'message': 'Question not found'}), 404
    
    return jsonify(question)

@questions_bp.put('/api/questions/<id>')
def update_question(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    new_question = request.get_json()
    idCategory = new_question['idCategory']
    content = new_question['content']
    
    cur.execute('UPDATE questions SET idCategory = %s, content = %s WHERE idQuestion = %s RETURNING *',
                (idCategory, content, id))
    updated_question = cur.fetchone()
    
    conn.commit()
    
    cur.close()
    conn.close()
    
    if updated_question is None:
        return jsonify({'message': 'Question not found'}), 404
    
    return jsonify(updated_question)

@questions_bp.get('/api/questions/<id>')
def get_question(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM questions WHERE idQuestion = %s', (id, ))
    question = cur.fetchone()
    
    if question is None:
        return jsonify({'message': 'Question not found'}), 404
    
    return jsonify(question)