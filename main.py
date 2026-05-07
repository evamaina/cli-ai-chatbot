from chatbot import Chatbot


def main():
    chatbot = Chatbot()

    print("CLI AI Chatbot")
    print("Type 'exit' to quit.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower() == "exit":
            print("Bot: Goodbye!")
            break

        bot_reply = chatbot.chat(user_message)
        print(f"Bot: {bot_reply}\n")


if __name__ == "__main__":
    main()