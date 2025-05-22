import threading
import asyncio
import os
import builtins
import nest_asyncio

from flask_app import app
from telegram_handler import start_telegram_bot
from smart_handler import smart_trade_loop
from report_scheduler import run_scheduler

nest_asyncio.apply()
builtins.bot_active = True

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def run_scheduler_safe():
    try:
        run_scheduler()
    except Exception as e:
        print("❌ Lỗi scheduler:", e)

def run_telegram_bot():
    try:
        asyncio.run(start_telegram_bot())
    except Exception as e:
        print("❌ Telegram Bot lỗi:", e)

def run_smart_trade():
    try:
        asyncio.run(smart_trade_loop())
    except Exception as e:
        print("❌ Smart Trade lỗi:", e)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    threading.Thread(target=run_scheduler_safe).start()
    threading.Thread(target=run_telegram_bot).start()
    threading.Thread(target=run_smart_trade).start()
