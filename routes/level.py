from flask import Blueprint, request, jsonify
from psycopg2 import connect, extras

level_bp = Blueprint('level', __name__)

host = 'localhost'
port = 5432
dbname = 'DBCyberTest'
user = 'postgres'
password = 'KM1013599968'

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn

@level_bp.get('/api/level')
def get_levels():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM level')
    levels = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(levels)

@level_bp.post('/api/level')
def create_level():
    new_level = request.get_json()
    difficulty = new_level['difficulty']

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO level (difficulty) VALUES (%s) RETURNING * ',
                (difficulty, ))
    
    new_created_level = cur.fetchone()
    print(new_created_level)
    conn.commit()
    
    cur.close()
    conn.close()

    return jsonify(new_created_level)

@level_bp.delete('/api/level/<id>')
def delete_level(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('DELETE FROM level WHERE idLevel = %s RETURNING * ', (id, ))
    level = cur.fetchone()
    
    conn.commit()
    
    conn.close()
    cur.close()
    
    if level is None:
        return jsonify({'message': 'Level not found'}), 404
    
    return jsonify(level)

@level_bp.put('/api/level/<id>')
def update_level(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    new_level = request.get_json()
    difficulty = new_level['difficulty']
    
    cur.execute('UPDATE level SET difficulty = %s WHERE idLevel = %s RETURNING *',
                (difficulty, id))
    updated_level = cur.fetchone()
    
    conn.commit()
    
    cur.close()
    conn.close()
    
    if updated_level is None:
        return jsonify({'message': 'Level not found'}), 404
    
    return jsonify(updated_level)

@level_bp.get('/api/level/<id>')
def get_level(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM level WHERE idLevel = %s', (id, ))
    level = cur.fetchone()
    
    if level is None:
        return jsonify({'message': 'Level not found'}), 404
    
    return jsonify(level)