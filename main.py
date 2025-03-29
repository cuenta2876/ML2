from fastapi import FastAPI
import uvicorn
import os
import psycopg2

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, ML2!"}

# Nuevo endpoint para verificar la conexión a la base de datos
@app.get("/test-db")
def test_db():
    DATABASE_URL = os.getenv("DATABASE_URL")  # Obtiene la URL de la base de datos desde las variables de entorno
    if not DATABASE_URL:
        return {"error": "DATABASE_URL no está configurada"}

    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")  # Consulta de prueba
        result = cursor.fetchone()
        conn.close()
        return {"message": "Conexión exitosa a la base de datos", "result": result}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Usa el puerto de Render si está disponible
    uvicorn.run(app, host="0.0.0.0", port=port)



