from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "CloudForge AI läuft 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello(name: str = "User"):
    return {"message": f"Hello {name}"}