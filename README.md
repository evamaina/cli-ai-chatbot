# CLI AI Chatbot (Step-by-Step Build)

This project is a beginner-friendly AI chatbot built in Python that runs in the command line (CLI).

The goal of this project is to learn how to:
- Work with AI APIs (OpenAI)
- Structure real-world Python projects
- Build features step by step
- Use Git and GitHub professionally (incremental commits)

---

## 🚀 Features (Current Progress)

### ✅ 1. Basic CLI Chatbot
- User can type messages in the terminal
- AI responds using OpenAI API
- Runs in a continuous loop until user exits

### ✅ 2. Session Memory
- Chatbot remembers conversation within the same session
- Uses a `conversation_history` list
- Sends full conversation to the model instead of a single message

Example:
You: My name is Eva
Bot: Nice to meet you, Eva.

You: What is my name?
Bot: Your name is Eva.


---

## 🛠️ Tech Stack

- Python
- OpenAI API
- python-dotenv (for environment variables)

---

## 📁 Project Structure
cli-ai-chatbot/
│
├── main.py # Main chatbot logic
├── .env # API key (not pushed to GitHub)
├── .gitignore # Ignore sensitive and unnecessary files
├── requirements.txt # Project dependencies
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/cli-ai-chatbot.git

cd cli-ai-chatbot


### 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate


### 3. Install dependencies
pip install -r requirements.txt


### 4. Add your API key

Create a `.env` file:
OPENAI_API_KEY=your_api_key_here



---

## ▶️ Run the chatbot



---

## 🧠 How Session Memory Works

- A list called `conversation_history` stores all messages
- Each user and bot message is appended
- The full history is sent to the AI model

This allows the chatbot to maintain context during a conversation.


## 👤 Author

Eva Maina
