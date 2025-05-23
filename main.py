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

# ✅ KHỞI ĐỘNG TẤT CẢ BẰNG asyncio.run() duy nhất
async def run_all():
    # Khởi động các task song song bằng asyncio
    telegram_task = asyncio.create_task(start_telegram_bot())
    trade_task = asyncio.create_task(smart_trade_loop())

    await asyncio.gather(telegram_task, trade_task)

if __name__ == "__main__":
    # 🔁 Flask & Scheduler chạy bằng thread
    threading.Thread(target=run_flask).start()
    threading.Thread(target=run_scheduler_safe).start()

    # 🔁 Telegram bot + Smart Trade chạy trong asyncio
    asyncio.run(run_all())
