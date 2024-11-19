from flask import Blueprint, request, jsonify
from psycopg2 import connect, extras

gameHasLevel_bp = Blueprint('gameHasLevel', __name__)

host = 'localhost'
port = 5432
dbname = 'CiberHero'
user = 'postgres'
password = 'nicolleMarquez07'

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn

@gameHasLevel_bp.get('/api/gameHasLevel')
def get_gameHasLevels():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM Game_has_Level')
    gameHasLevel = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(gameHasLevel)

@gameHasLevel_bp.post('/api/gameHasLevel')
def create_gameHasLevel():
    new_gameHasLevel = request.get_json()
    idGame = new_gameHasLevel['idGame']
    idUser = new_gameHasLevel['idUser']
    idLevel = new_gameHasLevel['idLevel']

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO Game_has_Level (idGame, idUser, idLevel) VALUES (%s, %s, %s) RETURNING * ',
                (idGame, idUser, idLevel))
    
    new_created_user = cur.fetchone()
    print(new_created_user)
    conn.commit()
    
    cur.close()
    conn.close()

    return jsonify(new_created_user)

@gameHasLevel_bp.delete('/api/gameHasLevel/<id>')
def delete_gameHasLevel(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('DELETE FROM Game_has_Level WHERE idGameHasLevel = %s RETURNING * ', (id, ))
    gameHasLevel = cur.fetchone()
    
    conn.commit()
    
    conn.close()
    cur.close()
    
    if gameHasLevel is None:
        return jsonify({'message': 'Game_has_Level not found'}), 404
    
    return jsonify(gameHasLevel)

@gameHasLevel_bp.put('/api/gameHasLevel/<id>')
def update_gameHasLevel(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    new_gameHasLevel = request.get_json()
    idGame = new_gameHasLevel['idGame']
    idUser = new_gameHasLevel['idUser']
    idLevel = new_gameHasLevel['idLevel']
    
    cur.execute('UPDATE Game_has_Level SET idGame = %s, idUser = %s, idLevel = %s WHERE idGameHasLevel = %s RETURNING *',
                (idGame, idUser, idLevel, id))
    updated_gameHasLevel = cur.fetchone()
    
    conn.commit()
    
    cur.close()
    conn.close()
    
    if updated_gameHasLevel is None:
        return jsonify({'message': 'Game_has_Level not found'}), 404
    
    return jsonify(updated_gameHasLevel)

@gameHasLevel_bp.get('/api/gameHasLevel/<id>')
def get_gameHasLevel(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM Game_has_Level WHERE idGameHasLevel = %s', (id, ))
    gameHasLevel = cur.fetchone()
    
    if gameHasLevel is None:
        return jsonify({'message': 'Game_has_Level not found'}), 404
    
    return jsonify(gameHasLevel)