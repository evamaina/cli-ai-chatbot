import sqlite3
import json
import numpy as np


class Memory:
    def __init__(self, db_name="chatbot.db"):
        self.db_name = db_name
        self.create_table()
        self.add_embedding_column_if_missing()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            embedding TEXT
        )
        """)

        conn.commit()
        conn.close()

    def save_message(self, role, content, embedding=None):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO messages (role, content, embedding) VALUES (?, ?, ?)",
            (role, content, embedding)
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
    
    def clear_memory(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM messages")

        conn.commit()
        conn.close()


    def get_history(self):
        return self.load_messages()
    
    
    def load_recent_messages(self, limit=10):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT role, content FROM messages
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        rows = cursor.fetchall()
        conn.close()

        rows.reverse()

        return [{"role": row[0], "content": row[1]} for row in rows]
    
    
    def add_embedding_column_if_missing(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("PRAGMA table_info(messages)")
        columns = [column[1] for column in cursor.fetchall()]

        if "embedding" not in columns:
            cursor.execute("ALTER TABLE messages ADD COLUMN embedding TEXT")

        conn.commit()
        conn.close()
    
    def load_messages_with_embeddings(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT role, content, embedding FROM messages
        WHERE embedding IS NOT NULL
        """)

        rows = cursor.fetchall()
        conn.close()

        return [
            {
                "role": row[0],
                "content": row[1],
                "embedding": json.loads(row[2])
            }
            for row in rows
        ]


    def cosine_similarity(self, vector_a, vector_b):
        a = np.array(vector_a)
        b = np.array(vector_b)

        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


    def search_relevant_messages(self, query_embedding, limit=5):
        messages = self.load_messages_with_embeddings()

        scored_messages = []

        for message in messages:
            score = self.cosine_similarity(query_embedding, message["embedding"])
            scored_messages.append((score, message))

        scored_messages.sort(reverse=True, key=lambda item: item[0])

        return [message for score, message in scored_messages[:limit]]