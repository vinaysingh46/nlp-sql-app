from fastapi import FastAPI
from pydantic import BaseModel
import time

from app.db import execute_query
from app.nlp import generate_sql
from app.analytics import track_query, get_stats

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
def query(req: QueryRequest):
    start = time.time()

    sql = generate_sql(req.question)
    result = execute_query(sql)

    execution_time = time.time() - start
    track_query(req.question, execution_time)

    return {
        "sql": sql,
        "result": result,
        "execution_time": execution_time
    }

@app.get("/stats")
def stats():
    return get_stats()