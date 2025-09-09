import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

DB_NAME = os.getenv("DB_NAME", "mydb")
DB_USER = os.getenv("DB_USER", "myuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "mypassword")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

app = FastAPI()

# allow same-origin (ingress) + quick dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_conn():
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
        host=DB_HOST, port=DB_PORT
    )

def ensure_table():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS texts (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT NOW()
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

class TextItem(BaseModel):
    content: str

@app.on_event("startup")
def startup_event():
    ensure_table()

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.post("/api/add")
def add_text(item: TextItem):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO texts (content) VALUES (%s)", (item.content,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Text added"}

@app.get("/api/list")
def list_texts():
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT id, content, created_at FROM texts ORDER BY id DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
