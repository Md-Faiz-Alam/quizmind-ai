import sqlite3

def init_db():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON")

    # ---------------- TOPICS ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS topics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    """)

    # ---------------- SUBTOPICS ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subtopics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        UNIQUE(topic_id, name),
        FOREIGN KEY (topic_id) REFERENCES topics(id) ON DELETE CASCADE
    )
    """)

    # ---------------- QUESTIONS ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic_id INTEGER NOT NULL,
        subtopic_id INTEGER NOT NULL,
        difficulty TEXT CHECK(difficulty IN ('easy','medium','hard')) DEFAULT 'easy',
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT CHECK(correct_answer IN ('a','b','c','d')) NOT NULL,
        explanation TEXT,
        tags TEXT,
        UNIQUE(question, subtopic_id),
        FOREIGN KEY (topic_id) REFERENCES topics(id) ON DELETE CASCADE,
        FOREIGN KEY (subtopic_id) REFERENCES subtopics(id) ON DELETE CASCADE
    )
    """)

    # ---------------- USERS ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # ---------------- RESULTS (QUIZ SUMMARY) ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        topic_id INTEGER NOT NULL,
        subtopic_id INTEGER NOT NULL,
        score INTEGER,
        total INTEGER,
        accuracy REAL,
        time_taken INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (topic_id) REFERENCES topics(id),
        FOREIGN KEY (subtopic_id) REFERENCES subtopics(id)
    )
    """)

    # ---------------- USER ANSWERS (DETAILED TRACKING) ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        question_id INTEGER NOT NULL,
        selected_answer TEXT CHECK(selected_answer IN ('a','b','c','d')),
        is_correct INTEGER CHECK(is_correct IN (0,1)),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
    )
    """)

    # ---------------- TOPIC SCORES (PROGRESS TRACKING) ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS topic_scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        topic_id INTEGER NOT NULL,
        rating INTEGER DEFAULT 1000,
        attempts INTEGER DEFAULT 0,
        correct INTEGER DEFAULT 0,
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(user_id, topic_id),
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (topic_id) REFERENCES topics(id) ON DELETE CASCADE
    )
    """)

    # ---------------- INDEXES (PERFORMANCE BOOST) ----------------
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_questions_topic ON questions(topic_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_questions_subtopic ON questions(subtopic_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_answers_user ON user_answers(user_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_results_user ON results(user_id)")

    conn.commit()
    conn.close()

    print("✅ Database initialized successfully with optimized schema!")


if __name__ == "__main__":
    init_db()