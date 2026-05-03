from flask import Blueprint, jsonify, request
from config import get_db
import hashlib

auth_bp = Blueprint("auth", __name__)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = hash_password(data.get("password"))

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING id",
            (name, email, password)
        )
        user_id = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return jsonify({
            "success": True,
            "user": {"id": user_id, "name": name, "email": email}
        })
    except Exception as e:
        conn.close()
        return jsonify({"success": False, "error": "Email already exists"}), 400

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = hash_password(data.get("password"))

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, email FROM users WHERE email=%s AND password=%s",
        (email, password)
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({
            "success": True,
            "user": {"id": user[0], "name": user[1], "email": user[2]}
        })
    else:
        return jsonify({"success": False, "error": "Invalid email or password"}), 401

@auth_bp.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"id": user[0], "name": user[1], "email": user[2]})
    return jsonify({"error": "User not found"}), 404