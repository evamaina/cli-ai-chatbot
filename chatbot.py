import os
from dotenv import load_dotenv
from openai import OpenAI
from memory import Memory
import json

load_dotenv()


class Chatbot:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.memory = Memory()
        self.conversation_history = self.memory.load_recent_messages(limit=10)

    def ask_ai(self):
        response = self.client.responses.create(
            model="gpt-5.2",
            instructions="You are a helpful beginner-friendly assistant.",
            input=self.conversation_history,
        )

        return response.output_text

    def chat(self, user_message):
        if user_message == "/clear":
            self.memory.clear_memory()
            self.conversation_history = []
            return "Memory cleared."

        if user_message == "/history":
            history = self.memory.get_history()
            if not history:
                return "No history found."

            formatted = ""
            for msg in history:
                formatted += f"{msg['role']}: {msg['content']}\n"

            return formatted

        if user_message == "/help":
            return (
                "Available commands:\n"
                "/clear - Clear all memory\n"
                "/history - Show conversation history\n"
                "/help - Show this message"
            )

        user_embedding = self.create_embedding(user_message)

        relevant_memories = self.memory.search_relevant_messages(
            query_embedding=user_embedding,
            limit=5
        )

        memory_context = [
            {
                "role": "system",
                "content": "Relevant past memories:\n" + "\n".join(
                    f"- {msg['role']}: {msg['content']}"
                    for msg in relevant_memories
                )
            }
        ]

        self.memory.save_message(
            "user",
            user_message,
            embedding=json.dumps(user_embedding)
        )

        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        bot_input = memory_context + self.conversation_history

        response = self.client.responses.create(
            model="gpt-5.2",
            instructions="You are a helpful beginner-friendly assistant.",
            input=bot_input,
        )

        bot_reply = response.output_text

        bot_embedding = self.create_embedding(bot_reply)

        self.memory.save_message(
            "assistant",
            bot_reply,
            embedding=json.dumps(bot_embedding)
        )

        self.conversation_history.append({
            "role": "assistant",
            "content": bot_reply
        })

        return bot_reply
    
    
    def create_embedding(self, text):
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text,
        )

        return response.data[0].embedding