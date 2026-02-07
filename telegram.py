import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def _validate_env():
    missing = []

    if not BOT_TOKEN:
        missing.append("TELEGRAM_BOT_TOKEN")
    if not CHAT_ID:
        missing.append("TELEGRAM_CHAT_ID")

    if missing:
        print("\n[ERROR] Missing required environment variables:")
        for var in missing:
            print(f"  - {var}")

        print(
            "\nFix this by adding them to a .env file or system environment.\n"
            "Example .env:\n"
            "TELEGRAM_BOT_TOKEN=your_bot_token_here\n"
            "TELEGRAM_CHAT_ID=your_chat_id_here\n"
        )
        sys.exit(1)


# Validate on import
_validate_env()


def send_message(text: str) -> bool:
    """
    Sends a Telegram message.
    Returns True if successful, False otherwise.
    """
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
