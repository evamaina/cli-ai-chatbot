# CLI AI Chatbot (Production-Ready Learning Project)

A command-line AI chatbot built in Python with **persistent memory**, **semantic search**, and **clean architecture**.

This project was built step by step to demonstrate:
- AI integration using OpenAI
- Memory systems (short-term + long-term + semantic)
- Clean, scalable Python architecture
- Real-world software engineering practices

---

## 🚀 Features

### 🤖 Chat Interface
- CLI-based chatbot
- Continuous interaction loop
- Clean user experience

---

### 🧠 Memory System

#### 1. Session Memory
- Tracks conversation during runtime

#### 2. Persistent Memory (SQLite)
- Stores all messages in `chatbot.db`
- Reloads conversation across sessions

#### 3. Smart Memory (Context Window)
- Only recent messages are sent to the model
- Prevents context overflow and improves performance

#### 4. Semantic Memory (Embeddings)
- Uses vector embeddings to understand meaning
- Retrieves relevant past messages based on similarity
- Implements a basic **RAG (Retrieval-Augmented Generation)** system

---

### ⚙️ Command System
/help → Show available commands
/history → View full stored conversation
/clear → Delete all memory


---

### 🏗️ Architecture (OOP + Clean Design)

The project follows **separation of concerns**:
main.py → CLI interface
chatbot.py → AI + conversation logic
memory.py → Database + semantic search



---

## 🛠️ Tech Stack

- Python
- OpenAI API
- SQLite
- NumPy (vector similarity)
- python-dotenv

---

## 📁 Project Structure
cli-ai-chatbot/
│
├── main.py
├── chatbot.py
├── memory.py
├── config.py # (optional improvement)
├── .env
├── .gitignore
├── requirements.txt
└── README.md




---

## ⚙️ Setup Instructions

git clone https://github.com/evamaina/cli-ai-chatbot.git

cd cli-ai-chatbot

### 1. Clone repository
python3 -m venv venv
source venv/bin/activate


---

### 3. Install dependencies

---

### 4. Add API key

Create a `.env` file:
OPENAI_API_KEY=your_api_key_here


---

## ▶️ Run the App



---

## 🧠 How Semantic Memory Works

1. User message → converted into an embedding
2. Stored messages → already have embeddings
3. Cosine similarity → finds most relevant past messages
4. Relevant memory + recent messages → sent to AI

This allows the chatbot to:
- Recall important past information
- Ignore irrelevant history
- Scale efficiently

---

## ⚡ Performance Considerations

- Context window is limited to recent messages
- Semantic search retrieves only top-N relevant memories
- Prevents excessive token usage and cost

---

## 🧩 Design Highlights (Interview-Ready)

- Retrieval-Augmented Generation (RAG)
- Separation of concerns
- Database-backed memory
- Vector similarity search
- Incremental Git-based development

---

## 📌 Future Improvements

- [ ] Streaming responses (real-time typing)
- [ ] Multiple chat sessions (threading)
- [ ] Web interface (Streamlit / FastAPI)
- [ ] Memory summarization
- [ ] Vector database (FAISS / Pinecone)

---



## 👤 Author

Eva Maina