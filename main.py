import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_ai(conversation_history):
    response = client.responses.create(
        model="gpt-5.2",
        instructions="You are a helpful beginner-friendly assistant.",
        input=conversation_history,
    )

    return response.output_text


def main():
    conversation_history = []

    print("CLI AI Chatbot with Session Memory")
    print("Type 'exit' to quit.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower() == "exit":
            print("Bot: Goodbye!")
            break

        conversation_history.append({
            "role": "user",
            "content": user_message
        })

        bot_reply = ask_ai(conversation_history)

        conversation_history.append({
            "role": "assistant",
            "content": bot_reply
        })

        print(f"Bot: {bot_reply}\n")


if __name__ == "__main__":
    main()