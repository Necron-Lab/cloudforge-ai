from fastapi import APIRouter
from app.services.llm import generate_response

router = APIRouter()

@router.get("/ask")
def ask(q: str):
    response = generate_response(q)
    return {"response": response}