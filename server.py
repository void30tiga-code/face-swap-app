from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Face Swap API Online"}

@app.get("/health")
def health():
    return {"ok": True}
