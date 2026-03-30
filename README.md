# nlp-sql-app

# NLP to SQL API (FastAPI Project)

## 📌 Description
This is an AI-powered backend project that converts natural language questions into SQL queries and returns results.

## 🚀 Features
- Convert user questions into SQL queries
- FastAPI based REST API
- Simple NLP (rule-based)
- Returns query result with execution time

## 🛠️ Tech Used
- Python
- FastAPI
- SQLite (or dummy data)
- NLP (basic logic)

## ▶️ How to Run
1. Open terminal
2. Run command:
   python -m uvicorn app.main:app --reload

3. Open browser:
   http://127.0.0.1:8000/docs

## 🧪 Example Query
```json
{
  "question": "how many students"
}
