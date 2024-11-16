from flask import Blueprint, request, jsonify
from psycopg2 import connect, extras

game_bp = Blueprint('game', __name__)

host = 'localhost'
port = 5432
dbname = 'DBCyberTest'
user = 'postgres'
password = 'KM1013599968'

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn

@game_bp.get('/api/game')
def get_games():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM game')
    games = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(games)

@game_bp.post('/api/game')
def create_game():
    new_game = request.get_json()
    idUser = new_game['idUser']
    startDate = new_game['startDate']
    endDate = new_game['endDate']
    finalScore = new_game['finalScore']

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO game (idUser, startDate, endDate, finalScore) VALUES (%s, %s, %s, %s) RETURNING * ',
                (idUser, startDate, endDate, finalScore))
    
    new_created_game = cur.fetchone()
    print(new_created_game)
    conn.commit()
    
    cur.close()
    conn.close()

    return jsonify(new_created_game)

@game_bp.delete('/api/game/<id>')
def delete_game(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('DELETE FROM game WHERE idGame = %s RETURNING * ', (id, ))
    game = cur.fetchone()
    
    conn.commit()
    
    conn.close()
    cur.close()
    
    if game is None:
        return jsonify({'message': 'Game not found'}), 404
    
    return jsonify(game)

@game_bp.put('/api/game/<id>')
def update_game(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    new_game = request.get_json()
    idUser = new_game['idUser']
    startDate = new_game['startDate']
    endDate = new_game['endDate']
    finalScore = new_game['finalScore']
    
    cur.execute('UPDATE game SET idUser = %s, startDate = %s, endDate = %s, finalScore = %s WHERE idGame = %s RETURNING *',
                (idUser, startDate, endDate, finalScore, id))
    updated_game = cur.fetchone()
    
    conn.commit()
    
    cur.close()
    conn.close()
    
    if updated_game is None:
        return jsonify({'message': 'Game not found'}), 404
    
    return jsonify(updated_game)

@game_bp.get('/api/game/<id>')
def get_game(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM game WHERE idGame = %s', (id, ))
    game = cur.fetchone()
    
    if game is None:
        return jsonify({'message': 'Game not found'}), 404
    
    return jsonify(game)