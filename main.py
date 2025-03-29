import os
from fastapi import FastAPI
import uvicorn
import psycopg2

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

def test_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("SELECT 1")
        cur.close()
        conn.close()
        return True
    except Exception as e:
        return str(e)

@app.get("/")
def read_root():
    return {"message": "Hello, ML2!"}

@app.get("/test-db")
def test_db():
    result = test_db_connection()
    if result is True:
        return {"status": "success", "message": "Connected to database!"}
    else:
        return {"status": "error", "message": result}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))  # Render asigna un puerto dinámico
    uvicorn.run(app, host="0.0.0.0", port=port)
