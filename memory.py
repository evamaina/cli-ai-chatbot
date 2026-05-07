import sqlite3


class Memory:
    def __init__(self, db_name="chatbot.db"):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        conn = self.connect()
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

    def save_message(self, role, content):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO messages (role, content) VALUES (?, ?)",
            (role, content)
        )

        conn.commit()
        conn.close()

    def load_messages(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT role, content FROM messages ORDER BY id ASC")
        rows = cursor.fetchall()

        conn.close()

        return [{"role": row[0], "content": row[1]} for row in rows]