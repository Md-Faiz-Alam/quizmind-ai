import os
from flask import Flask
from flask_cors import CORS
from routes.quiz_routes import quiz_bp
from routes.auth_routes import auth_bp
from routes.result_routes import result_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(quiz_bp, url_prefix="/api/quiz")
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(result_bp, url_prefix="/api/results")

@app.route("/")
def home():
    return {"message": "QuizMind AI Backend Running 🚀"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)