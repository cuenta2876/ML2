from fastapi import FastAPI
from routes import home  # Solo si ejecutas uvicorn con `PYTHONPATH`


import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, ML2!"}

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 8000))  # Usa el puerto de Render si está disponible
    uvicorn.run(app, host="0.0.0.0", port=port)






