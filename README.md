# CLI AI Chatbot (Step-by-Step Build)

A beginner-friendly AI chatbot built in Python that runs in the command line (CLI).

This project is built **step by step**, focusing on:
- Understanding AI integration
- Writing clean, modular code
- Using GitHub professionally (incremental commits)

---

## 🚀 Features (Current Progress)

### ✅ 1. CLI Chat Interface
- Chat with AI directly in the terminal
- Continuous loop until exit

### ✅ 2. Session Memory
- Remembers messages during runtime
- Uses a conversation history list

### ✅ 3. Persistent Memory (SQLite)
- Stores messages in a database (`chatbot.db`)
- Loads past conversations when restarting the app

### ✅ 4. Smart Memory (Optimized Context)
- Sends only recent messages to the AI (last N messages)
- Improves performance and scalability

### ✅ 5. Command System
Built-in commands:
/help → Show available commands
/history → Show full conversation history
/clear → Delete all stored memory


---

## 🛠️ Tech Stack

- Python
- OpenAI API
- SQLite (built-in database)
- python-dotenv

---

## 📁 Project Structure

cli-ai-chatbot/
│
├── main.py # Entry point (CLI loop)
├── chatbot.py # Chatbot logic (AI + memory)
├── memory.py # Database layer (SQLite)
├── .env # API key (not committed)
├── .gitignore
├── requirements.txt
└── README.md



---

## ⚙️ Setup Instructions

### 1. Clone repository
git clone https://github.com/evamaina/cli-ai-chatbot.git

cd cli-ai-chatbot



### 2. Create virtual environment

python3 -m venv venv
source venv/bin/activate


### 3. Install dependencies
pip install -r requirements.txt


### 4. Add API key

Create `.env` file:
OPENAI_API_KEY=your_api_key_here


---

## ▶️ Run the App




---

## 🧠 How Memory Works

### 1. Persistent Storage
- Messages are saved in SQLite (`chatbot.db`)
- Each message has:
  - role (user / assistant)
  - content

### 2. Smart Context Loading
- Only recent messages are sent to the AI
- Full history remains stored in the database

This balances:
- Context awareness ✅
- Performance ⚡
- Scalability 📈

---

## 🧩 Architecture Design

The project follows **separation of concerns**:

- `main.py` → CLI interface
- `chatbot.py` → AI + conversation logic
- `memory.py` → database operations

This makes the code:
- Easier to maintain
- Easier to extend
- Closer to production-level design

---





## 👤 Author

Eva Maina
