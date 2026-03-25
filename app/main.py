from fastapi import FastAPI
from app.routers import health, hello, ai

app = FastAPI()

app.include_router(health.router)
app.include_router(hello.router)
app.include_router(ai.router)