from flask import Flask, request, jsonify
from psycopg2 import connect, extras
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()

host = 'localhost'
port = 5432
dbname = 'DBCyberTest'
user = 'postgres'
password = 'KM1013599968'

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn

@app.get('/api/users')
def get_users():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(users)

@app.post('/api/users')
def create_user():
    new_user = request.get_json()
    idCard = new_user['idCard']
    names = new_user['names']
    surnames = new_user['surnames']
    email = new_user['email']
    password = Fernet(key).encrypt(bytes(new_user['password'], 'utf-8'))
    score = new_user['score']

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO users (idCard, names, surnames, email, password, score) VALUES (%s, %s, %s, %s, %s, %s) RETURNING * ',
                (idCard, names, surnames, email, password, score))
    
    new_created_user = cur.fetchone()
    print(new_created_user)
    conn.commit()
    
    cur.close()
    conn.close()

    return jsonify(new_created_user)

@app.delete('/api/users/<id>')
def delete_user(id):
    
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('DELETE FROM users WHERE idUser = %s RETURNING * ', (id, ))
    user = cur.fetchone()
    
    conn.commit()
    
    conn.close()
    cur.close()
    
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    
    return jsonify(user)

@app.put('/api/users/<id>')
def update_user(id):
    
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    new_user = request.get_json()
    idCard = new_user['idCard']
    names = new_user['names']
    surnames = new_user['surnames']
    email = new_user['email']
    password = Fernet(key).encrypt(bytes(new_user['password'], 'utf-8'))
    score = new_user['score']
    
    cur.execute('UPDATE users SET idCard = %s, names = %s, surnames = %s, email = %s, password = %s, score = %s WHERE idUser = %s RETURNING *',
                (idCard, names, surnames, email, password, score, id))
    updated_user = cur.fetchone()
    
    conn.commit()
    
    cur.close()
    conn.close()
    
    if updated_user is None:
        return jsonify({'message': 'User not found'}), 404
    
    return jsonify(updated_user)

@app.get('/api/users/<id>')
def get_user(id):
    
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM users WHERE idUser = %s', (id, ))
    user = cur.fetchone()
    
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)