from flask import Blueprint, request, jsonify
from psycopg2 import connect, extras

answers_bp = Blueprint('answers', __name__)

host = 'localhost'
port = 5432
dbname = 'DBCyberTest'
user = 'postgres'
password = 'KM1013599968'

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn

@answers_bp.get('/api/answers')
def get_answers():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM answers')
    answers = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(answers)

@answers_bp.post('/api/answers')
def create_answer():
    new_answer = request.get_json()
    idQuestion = new_answer['idQuestion']
    answer = new_answer['answer']
    isCorrect = new_answer['isCorrect']

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO answers (idQuestion, answer, isCorrect) VALUES (%s, %s, %s) RETURNING * ',
                (idQuestion, answer, isCorrect))
    
    new_created_answer = cur.fetchone()
    print(new_created_answer)
    conn.commit()
    
    cur.close()
    conn.close()

    return jsonify(new_created_answer)

@answers_bp.delete('/api/answers/<id>')
def delete_answer(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('DELETE FROM answers WHERE idAnswer = %s RETURNING * ', (id, ))
    answer = cur.fetchone()
    
    conn.commit()
    
    conn.close()
    cur.close()
    
    if answer is None:
        return jsonify({'message': 'Answer not found'}), 404
    
    return jsonify(answer)

@answers_bp.put('/api/answers/<id>')
def update_answers(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    new_answer = request.get_json()
    idQuestion = new_answer['idQuestion']
    answer = new_answer['answer']
    isCorrect = new_answer['isCorrect']
    
    cur.execute('UPDATE answers SET idQuestion = %s, answer = %s, isCorrect = %s WHERE idAnswer = %s RETURNING *',
                (idQuestion, answer, isCorrect, id))
    updated_answer = cur.fetchone()
    
    conn.commit()
    
    cur.close()
    conn.close()
    
    if updated_answer is None:
        return jsonify({'message': 'Answer not found'}), 404
    
    return jsonify(updated_answer)

@answers_bp.get('/api/answers/<id>')
def get_answer(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM answers WHERE idAnswer = %s', (id, ))
    answer = cur.fetchone()
    
    if answer is None:
        return jsonify({'message': 'Answer not found'}), 404
    
    return jsonify(answer)