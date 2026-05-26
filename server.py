from fastapi import FastAPI
import os

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN")

@app.get("/")
def home():
    return {
        "status": "Bot Online",
        "telegram": "connected" if BOT_TOKEN else "token missing"
    }

@app.get("/webhook")
def webhook():
    return {
        "message": "Telegram bot ready"
    }
