import os
import requests


BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_message(text: str) -> bool:
    """
    Sends a Telegram message.
    Returns True if successful, False otherwise.
    """
    if not BOT_TOKEN or not CHAT_ID:
        return False

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        return response.status_code == 200
    except requests.RequestException:
        return False
