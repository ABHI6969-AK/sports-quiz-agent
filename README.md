# 🏆 AI Sports Quiz Generator

An AI-powered Sports Quiz Generator built using **Streamlit**, **Groq LLM**, **ChromaDB**, and **DuckDuckGo Search**. The application generates intelligent sports quizzes using Retrieval-Augmented Generation (RAG) and the latest sports information.

---

## 🚀 Live Demo

🔗 Streamlit App: https://sports-quiz-agent-dxsz2hprepix6ufgfjsx3m.streamlit.app/


---

## 📌 Features

- 🤖 AI-generated sports quizzes
- ⚽ Multiple sports support
- 🎯 Difficulty selection (Easy, Medium, Hard)
- 🧠 Retrieval-Augmented Generation (RAG)
- 📰 Latest sports news integration
- 📚 ChromaDB vector database
- 💯 Automatic quiz scoring
- 🎨 Modern Streamlit UI

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API (LLM)
- ChromaDB
- DuckDuckGo Search
- Sentence Transformers
- Hugging Face
- JSON

---

## 📂 Project Structure

```
sports-quiz-agent/
│
├── app.py
├── requirements.txt
├── styles.css
│
├── data/
│   └── sports_facts.json
│
├── chroma_db/
│
├── src/
│   ├── config.py
│   ├── database.py
│   ├── generator.py
│   ├── parser.py
│   ├── prompts.py
│   ├── search.py
│   └── utils.py
│
├── test_db.py
├── test_generator.py
└── test_search.py
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/ABHI6969-AK/sports-quiz-agent.git
```

Go into the project

```bash
cd sports-quiz-agent
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root folder.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. User selects a sport.
2. User selects a difficulty level.
3. The application retrieves relevant sports knowledge from ChromaDB.
4. Latest sports information is fetched using DuckDuckGo Search.
5. Both sources are combined as context.
6. Groq LLM generates five multiple-choice questions.
7. The user answers the questions.
8. The application calculates and displays the final score.



---

## 🎯 Future Improvements

- User authentication
- Leaderboard
- Timer-based quizzes
- Multiplayer mode
- AI explanations for answers
- Voice-based quiz generation
- Additional sports categories

---

## 👨‍💻 Author

**Abhinav Kola**

GitHub:
https://github.com/ABHI6969-AK

---

## 📄 License

This project is developed for educational and learning purposes.
