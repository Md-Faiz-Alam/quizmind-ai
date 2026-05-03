from flask import Blueprint, jsonify, request
from config import get_db

result_bp = Blueprint("result", __name__)

@result_bp.route("/save", methods=["POST"])
def save_result():
    data = request.get_json()
    user_id = data.get("user_id")
    subtopic_id = data.get("subtopic_id")
    score = data.get("score")
    total = data.get("total")
    time_taken = data.get("time_taken")
    accuracy = round((score / total) * 100, 2) if total > 0 else 0

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT topic_id FROM subtopics WHERE id = %s", (subtopic_id,))
    row = cursor.fetchone()
    topic_id = row[0] if row else 1

    cursor.execute("""
        INSERT INTO results (user_id, topic_id, subtopic_id, score, total, accuracy, time_taken)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (user_id, topic_id, subtopic_id, score, total, accuracy, time_taken))

    conn.commit()
    conn.close()
    return jsonify({"success": True, "accuracy": accuracy})

@result_bp.route("/history/<int:user_id>", methods=["GET"])
def get_history(user_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT r.id, s.name, r.score, r.total, r.accuracy, r.time_taken, r.created_at
        FROM results r
        JOIN subtopics s ON r.subtopic_id = s.id
        WHERE r.user_id = %s
        ORDER BY r.created_at DESC
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    history = []
    for row in rows:
        history.append({
            "id": row[0],
            "subtopic": row[1],
            "score": row[2],
            "total": row[3],
            "accuracy": row[4],
            "time_taken": row[5],
            "date": str(row[6])
        })

    return jsonify(history)

@result_bp.route("/analytics/<int:user_id>", methods=["GET"])
def get_analytics(user_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT t.name,
               COUNT(r.id) as attempts,
               ROUND(AVG(r.accuracy)::numeric, 2) as avg_accuracy,
               MAX(r.accuracy) as best_score
        FROM results r
        JOIN subtopics s ON r.subtopic_id = s.id
        JOIN topics t ON s.topic_id = t.id
        WHERE r.user_id = %s
        GROUP BY t.name
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    analytics = []
    for row in rows:
        analytics.append({
            "topic": row[0],
            "attempts": row[1],
            "avg_accuracy": float(row[2]) if row[2] else 0,
            "best_score": float(row[3]) if row[3] else 0
        })

    return jsonify(analytics)

@result_bp.route("/weak-areas/<int:user_id>", methods=["GET"])
def get_weak_areas(user_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, ROUND(AVG(r.accuracy)::numeric, 2) as avg_accuracy
        FROM results r
        JOIN subtopics s ON r.subtopic_id = s.id
        WHERE r.user_id = %s
        GROUP BY s.name
        HAVING AVG(r.accuracy) < 60
        ORDER BY avg_accuracy ASC
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    weak = []
    for row in rows:
        weak.append({
            "subtopic": row[0],
            "accuracy": float(row[1]) if row[1] else 0
        })

    return jsonify(weak)

@result_bp.route("/topics/<int:user_id>", methods=["GET"])
def get_topics(user_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT t.id, t.name,
               COUNT(DISTINCT s.id) as subtopic_count
        FROM topics t
        JOIN subtopics s ON s.topic_id = t.id
        GROUP BY t.id, t.name
        ORDER BY t.id
    """)

    rows = cursor.fetchall()
    conn.close()

    topics = []
    for row in rows:
        topics.append({
            "id": row[0],
            "name": row[1],
            "subtopic_count": row[2]
        })

    return jsonify(topics)

@result_bp.route("/subtopics/<int:topic_id>", methods=["GET"])
def get_subtopics(topic_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name FROM subtopics WHERE topic_id = %s ORDER BY id
    """, (topic_id,))

    rows = cursor.fetchall()
    conn.close()

    return jsonify([{"id": r[0], "name": r[1]} for r in rows])