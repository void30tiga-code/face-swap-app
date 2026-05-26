from fastapi import FastAPI, Request
import os
import urllib.request
import json

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_message(chat_id, text):
    req = urllib.request.Request(
        f"{API}/sendMessage",
        data=json.dumps({
            "chat_id": chat_id,
            "text": text
        }).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    urllib.request.urlopen(req)

@app.get("/")
def home():
    return {"status": "photo mode ready"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    if "message" in data:
        msg = data["message"]
        chat_id = msg["chat"]["id"]

        if "photo" in msg:
            send_message(chat_id, "📸 Foto diterima.\nFace swap processing...")
        else:
            send_message(chat_id, "Kirim foto untuk diproses face swap")

    return {"ok": True}
