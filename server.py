from fastapi import FastAPI, Request
import os
import urllib.request
import json

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.get("/")
def home():
    return {"status": "connected"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = "✅ Bot aktif dan membalas"

        req = urllib.request.Request(
            f"{API}/sendMessage",
            data=json.dumps({
                "chat_id": chat_id,
                "text": text
            }).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )

        urllib.request.urlopen(req)

    return {"ok": True}
