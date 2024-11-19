from flask import Blueprint, request, jsonify
from psycopg2 import connect, extras

questions_bp = Blueprint('questions', __name__)

# Configuración de la conexión a la base de datos
host = 'localhost'
port = 5432
dbname = 'CiberHero'
user = 'postgres'
password = 'nicolleMarquez07'

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn

@questions_bp.route('/api/questions/process', methods=['GET'])
def process_questions():
    # Obtener el nivel y las respuestas de los parámetros de la URL
    level = request.args.get('level', type=int)
    user_answers = request.args.get('answers', default="{}", type=str)

    # Convertir las respuestas en un diccionario
    try:
        user_answers = eval(user_answers)  # Evalúa la cadena como un diccionario (Úsalo con cuidado)
        if not isinstance(user_answers, dict):
            raise ValueError
    except Exception:
        return jsonify({"error": "El parámetro 'answers' debe ser un diccionario en formato JSON."}), 400

    # Validar que se envíe un nivel válido
    if level is None:
        return jsonify({"error": "Falta el parámetro 'level' o no es un entero válido."}), 400

    # Conexión a la base de datos
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    # Obtener las preguntas del nivel correspondiente
    query = """
        SELECT q.idQuestion, q.content AS originalQuestion
        FROM Questions q
        INNER JOIN Categories c ON q.idCategory = c.idCategory
        INNER JOIN Monsters m ON c.idMonsters = m.idMonsters
        WHERE m.idLevel = %s;
    """
    cur.execute(query, (level,))
    questions = cur.fetchall()

    # Procesar las respuestas del usuario
    transformed_questions = []
    for question in questions:
        question_id = question['idQuestion']
        user_answer = user_answers.get(str(question_id), None)

        # Obtener la respuesta correcta de la base de datos
        cur.execute("""
            SELECT isCorrect FROM Answers
            WHERE idQuestion = %s AND isCorrect = TRUE;
        """, (question_id,))
        correct_answer = cur.fetchone()

        # Verificar si la respuesta es correcta
        is_correct = user_answer == correct_answer['isCorrect'] if correct_answer else False

        # Transformar la pregunta si es incorrecta
        transformed_question = {
            "idQuestion": question_id,
            "originalQuestion": question['originalQuestion'],
            "transformedQuestion": None
        }
        if not is_correct:
            transformed_question["transformedQuestion"] = f"¿Puedes explicar mejor: {question['originalQuestion']}?"

        transformed_questions.append(transformed_question)

    cur.close()
    conn.close()

    return jsonify({
        "level": level,
        "transformedQuestions": transformed_questions
})