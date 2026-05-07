def chat(self, user_message):
    # Handle commands
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

    # Normal chat flow
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