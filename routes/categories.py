from flask import Blueprint, request, jsonify
from psycopg2 import connect, extras

categories_bp = Blueprint('categories', __name__)

host = 'localhost'
port = 5432
dbname = 'CiberHero'
user = 'postgres'
password = 'nicolleMarquez07'

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn

@categories_bp.get('/api/categories')
def get_categories():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM categories')
    categories = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return jsonify(categories)

@categories_bp.post('/api/categories')
def create_categories():
    new_category = request.get_json()
    idMonsters = new_category['idMonsters']
    category = new_category['category']

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO categories (idMonsters, category) VALUES (%s, %s) RETURNING * ',
                (idMonsters, category))
    
    new_created_category = cur.fetchone()
    print(new_created_category)
    conn.commit()
    
    cur.close()
    conn.close()

    return jsonify(new_created_category)

@categories_bp.delete('/api/categories/<id>')
def delete_category(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('DELETE FROM categories WHERE idCategory = %s RETURNING * ', (id, ))
    category = cur.fetchone()
    
    conn.commit()
    
    conn.close()
    cur.close()
    
    if category is None:
        return jsonify({'message': 'Category not found'}), 404
    
    return jsonify(category)

@categories_bp.put('/api/categories/<id>')
def update_category(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    new_category = request.get_json()
    idMonsters = new_category['idMonsters']
    category = new_category['category']
    
    cur.execute('UPDATE categories SET idMonsters = %s, category = %s WHERE idCategory = %s RETURNING *',
                (idMonsters, category, id))
    updated_category = cur.fetchone()
    
    conn.commit()
    
    cur.close()
    conn.close()
    
    if updated_category is None:
        return jsonify({'message': 'Category not found'}), 404
    
    return jsonify(updated_category)

@categories_bp.get('/api/categories/<id>')
def get_category(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM categories WHERE idCategory = %s', (id, ))
    category = cur.fetchone()
    
    if category is None:
        return jsonify({'message': 'Category not found'}), 404
    
    return jsonify(category)