import os
from dotenv import load_dotenv
from openai import OpenAI
from memory import create_table, save_message, load_messages

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
    create_table()

    # Load past memory
    conversation_history = load_messages()

    print("CLI AI Chatbot with Persistent Memory")
    print("Type 'exit' to quit.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower() == "exit":
            print("Bot: Goodbye!")
            break

        # Save user message
        save_message("user", user_message)

        conversation_history.append({
            "role": "user",
            "content": user_message
        })

        bot_reply = ask_ai(conversation_history)

        # Save bot reply
        save_message("assistant", bot_reply)

        conversation_history.append({
            "role": "assistant",
            "content": bot_reply
        })

        print(f"Bot: {bot_reply}\n")


if __name__ == "__main__":
    main()