import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_ai(user_message):
    response = client.responses.create(
        model="gpt-5.2",
        instructions="You are a helpful beginner-friendly assistant.",
        input=user_message,
    )

    return response.output_text


def main():
    print("CLI AI Chatbot")
    print("Type 'exit' to quit.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower() == "exit":
            print("Bot: Goodbye!")
            break

        bot_reply = ask_ai(user_message)
        print(f"Bot: {bot_reply}\n")


if __name__ == "__main__":
    main()