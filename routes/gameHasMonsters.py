from flask import Blueprint, request, jsonify
from psycopg2 import connect, extras

gameHasMonsters_bp = Blueprint('gameHasMonsters', __name__)

host = 'localhost'
port = 5432
dbname = 'DBCyberTest'
user = 'postgres'
password = 'KM1013599968'

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn

@gameHasMonsters_bp.get('/api/gameHasMonsters')
def get_gameHasMonsters():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM Game_has_Monsters')
    gameHasMonsters = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(gameHasMonsters)

@gameHasMonsters_bp.post('/api/gameHasMonsters')
def create_gameHasMonsters():
    new_gameHasMonsters = request.get_json()
    idGame = new_gameHasMonsters['idGame']
    idUser = new_gameHasMonsters['idUser']
    idMonsters = new_gameHasMonsters['idMonsters']
    idLevel = new_gameHasMonsters['idLevel']

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO Game_has_Monsters (idGame, idUser, idMonsters, idLevel) VALUES (%s, %s, %s, %s) RETURNING * ',
                (idGame, idUser, idMonsters, idLevel))
    
    new_created_gameHasMonster = cur.fetchone()
    print(new_created_gameHasMonster)
    conn.commit()
    
    cur.close()
    conn.close()

    return jsonify(new_created_gameHasMonster)

@gameHasMonsters_bp.delete('/api/gameHasMonsters/<id>')
def delete_gameHasMonster(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('DELETE FROM Game_has_Monsters WHERE idGameHasMonsters = %s RETURNING * ', (id, ))
    gameHasMonsters = cur.fetchone()
    
    conn.commit()
    
    conn.close()
    cur.close()
    
    if gameHasMonsters is None:
        return jsonify({'message': 'Game_has_Monsters not found'}), 404
    
    return jsonify(gameHasMonsters)

@gameHasMonsters_bp.put('/api/gameHasMonsters/<id>')
def update_gameHasMonsters(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    new_gameHasMonsters = request.get_json()
    idGame = new_gameHasMonsters['idGame']
    idUser = new_gameHasMonsters['idUser']
    idMonsters = new_gameHasMonsters['idMonsters']
    idLevel = new_gameHasMonsters['idLevel']
    
    cur.execute('UPDATE Game_has_Monsters SET idGame = %s, idUser = %s, idMonsters = %s, idLevel = %s WHERE idGameHasMonsters = %s RETURNING *',
                (idGame, idUser, idMonsters, idLevel, id))
    updated_gameHasMonsters = cur.fetchone()
    
    conn.commit()
    
    cur.close()
    conn.close()
    
    if updated_gameHasMonsters is None:
        return jsonify({'message': 'Game_has_Monsters not found'}), 404
    
    return jsonify(updated_gameHasMonsters)

@gameHasMonsters_bp.get('/api/gameHasMonsters/<id>')
def get_updated_gameHasMonsters(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM Game_has_Monsters WHERE idGameHasMonsters = %s', (id, ))
    gameHasMonsters = cur.fetchone()
    
    if gameHasMonsters is None:
        return jsonify({'message': 'Game_has_Monsters not found'}), 404
    
    return jsonify(gameHasMonsters)