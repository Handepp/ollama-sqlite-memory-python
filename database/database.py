import sqlite3
import time

DB_NAME = "database/history.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions (
        session_id TEXT PRIMARY KEY,
        created_at REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT,
        role TEXT,
        content TEXT,
        timestamp REAL
    )
    """)

    conn.commit()
    conn.close()

def create_session(session_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO sessions (session_id, created_at)
    VALUES (?, ?)
    """, (session_id, time.time()))

    conn.commit()
    conn.close()

def save_message(session_id, role, content):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO messages (session_id, role, content, timestamp)
    VALUES (?, ?, ?, ?)
    """, (session_id, role, content, time.time()))

    conn.commit()
    conn.close()

def get_messages(session_id, Limit=10):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT role, content
    FROM messages
    WHERE session_id = ?
    ORDER BY timestamp DESC
    LIMIT ?
    """, (session_id, Limit))  

    rows = cursor.fetchall()
    conn.close()

    rows = rows[::-1]

    # convert to Ollama format
    messages = []
    for role, content in rows:
        messages.append({
            "role": role,
            "content": content
        })

    return messages