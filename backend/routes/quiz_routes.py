from flask import Blueprint, jsonify
from config import get_db

quiz_bp = Blueprint("quiz", __name__)

@quiz_bp.route("/questions/<int:subtopic_id>", methods=["GET"])
def get_questions(subtopic_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, question, option_a, option_b, option_c, option_d,
               correct_answer, explanation
        FROM questions
        WHERE subtopic_id = %s
    """, (subtopic_id,))

    rows = cursor.fetchall()
    conn.close()

    questions = []
    for row in rows:
        questions.append({
            "id": row[0],
            "question": row[1],
            "options": {
                "a": row[2],
                "b": row[3],
                "c": row[4],
                "d": row[5]
            },
            "correct_answer": row[6],
            "explanation": row[7]
        })

    return jsonify(questions)