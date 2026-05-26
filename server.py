from fastapi import FastAPI
import os

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN")

@app.get("/")
def home():
    return {
        "status": "online",
        "token": "detected" if BOT_TOKEN else "missing"
    }

@app.get("/webhook")
def webhook():
    return {"message": "ready"}
