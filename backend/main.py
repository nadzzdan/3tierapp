from fastapi import FastAPI
from pydantic import BaseModel
import os
import psycopg2

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASS = os.getenv("DB_PASS", "apppass")

class TextInput(BaseModel):
    text: str

def get_conn():
    return psycopg2.connect(
        host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS
    )

@app.get("/health")
@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.post("/submit")
@app.post("/api/submit")
def submit_text(item: TextInput):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO texts (content) VALUES (%s)", (item.text,))
    conn.commit()
    cur.close()
    conn.close()
    return {"status": "success"}

@app.get("/texts")
@app.get("/api/texts")
def get_texts():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT content FROM texts ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [r[0] for r in rows]
