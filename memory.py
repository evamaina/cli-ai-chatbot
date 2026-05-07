import sqlite3

DB_NAME = "chatbot.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT NOT NULL,
        content TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def save_message(role, content):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages (role, content) VALUES (?, ?)",
        (role, content)
    )

    conn.commit()
    conn.close()


def load_messages():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT role, content FROM messages ORDER BY id ASC")
    rows = cursor.fetchall()

    conn.close()

    return [{"role": row[0], "content": row[1]} for row in rows]