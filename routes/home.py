from fastapi import APIRouter

router = APIRouter()

@router.get("/home")
def home():
    return {"message": "Página principal de ML2"}
