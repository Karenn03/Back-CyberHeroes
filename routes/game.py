from flask import Blueprint, request, jsonify
from psycopg2 import connect, extras

game_bp = Blueprint('game', __name__)

host = 'localhost'
port = 5432
dbname = 'CiberHero'
user = 'postgres'
password = 'nicolleMarquez07'

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
    try:
        new_game = request.get_json()
        required_fields = ['idUser', 'startDate', 'endDate', 'finalScore']
        for field in required_fields:
            if field not in new_game:
                return jsonify({'error': f'Missing field: {field}'}), 400

        idUser = new_game['idUser']
        startDate = new_game['startDate']
        endDate = new_game['endDate']
        finalScore = new_game['finalScore']

        print(f"Received game data: {new_game}")  # Depuración para verificar el JSON recibido

        conn = get_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        # Asegurarse de que la tabla se llama correctamente 'game' en minúsculas
        cur.execute(
            'INSERT INTO game (idUser, startDate, endDate, finalScore) VALUES (%s, %s, %s, %s) RETURNING idGame',
            (idUser, startDate, endDate, finalScore)
        )
        
        # Obtener el resultado de la consulta
        result = cur.fetchone()
        print(f"Result of INSERT query: {result}")  # Depuración para verificar el valor retornado

        if result is None:
            return jsonify({'error': 'INSERT query did not return an idGame'}), 500

        idGame = result['idGame']

        # Insertar en game_has_level
        cur.execute(
            'INSERT INTO game_has_level (idGame, idUser, idLevel) VALUES (%s, %s, %s)',
            (idGame, idUser, idLevel)
        )

        # Asociar monstruos del nivel a game_has_monsters
        cur.execute('SELECT idMonsters FROM monsters WHERE idLevel = %s', (idLevel,))
        monsters = cur.fetchall()
        for monster in monsters:
            cur.execute(
                'INSERT INTO game_has_monsters (idGame, idUser, idMonsters, idLevel) VALUES (%s, %s, %s, %s)',
                (idGame, idUser, monster['idMonsters'], idLevel)
            )

        conn.commit()
        return jsonify({'message': 'Game created and associations updated successfully', 'idGame': idGame})
    
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 400

    finally:
        cur.close()
        conn.close()



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