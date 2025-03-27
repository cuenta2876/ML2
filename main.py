from fastapi import FastAPI
from app.routes import home

app = FastAPI()

app.include_router(home.router)

@app.get("/")
def root():
    return {"message": "Bienvenido a ML2"}
