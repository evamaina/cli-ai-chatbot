import os
from dotenv import load_dotenv
from openai import OpenAI
from memory import Memory

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
        self.memory.save_message("user", user_message)

        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        bot_reply = self.ask_ai()

        self.memory.save_message("assistant", bot_reply)

        self.conversation_history.append({
            "role": "assistant",
            "content": bot_reply
        })

        return bot_reply