from flask import Blueprint, request, jsonify
from psycopg2 import connect, extras

monsters_bp = Blueprint('monsters', __name__)

host = 'localhost'
port = 5432
dbname = 'DBCyberTest'
user = 'postgres'
password = 'KM1013599968'

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn

@monsters_bp.get('/api/monsters')
def get_monsters():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM monsters')
    monsters = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(monsters)

@monsters_bp.post('/api/monsters')
def create_monster():
    new_monster = request.get_json()
    idLevel = new_monster['idLevel']
    name = new_monster['name']
    description = new_monster['description']

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO monsters (idLevel, name, description) VALUES (%s, %s, %s) RETURNING * ',
                (idLevel, name, description))
    
    new_created_monster = cur.fetchone()
    print(new_created_monster)
    conn.commit()
    
    cur.close()
    conn.close()

    return jsonify(new_created_monster)

@monsters_bp.delete('/api/monsters/<id>')
def delete_monster(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('DELETE FROM monsters WHERE idMonsters = %s RETURNING * ', (id, ))
    monster = cur.fetchone()
    
    conn.commit()
    
    conn.close()
    cur.close()
    
    if monster is None:
        return jsonify({'message': 'Monster not found'}), 404
    
    return jsonify(monster)

@monsters_bp.put('/api/monsters/<id>')
def update_monster(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    new_monster = request.get_json()
    idLevel = new_monster['idLevel']
    name = new_monster['name']
    description = new_monster['description']
    
    cur.execute('UPDATE monsters SET idLevel = %s, name = %s, description = %s WHERE idMonsters = %s RETURNING *',
                (idLevel, name, description, id))
    updated_monster = cur.fetchone()
    
    conn.commit()
    
    cur.close()
    conn.close()
    
    if updated_monster is None:
        return jsonify({'message': 'Monster not found'}), 404
    
    return jsonify(updated_monster)

@monsters_bp.get('/api/monsters/<id>')
def get_monster(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM monsters WHERE idMonsters = %s', (id, ))
    monster = cur.fetchone()
    
    if monster is None:
        return jsonify({'message': 'Monster not found'}), 404
    
    return jsonify(monster)