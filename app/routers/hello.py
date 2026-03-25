from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def hello(name: str = "User"):
    return {"message": f"Hello {name}"}