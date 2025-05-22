# main.py

import threading
import asyncio
import builtins
import os
import nest_asyncio

from flask_app import app
from telegram_handler import start_telegram_bot
from smart_handler import smart_trade_loop
from report_scheduler import run_scheduler

# ✅ Cho phép tái sử dụng event loop trên môi trường như Replit, Railway
nest_asyncio.apply()
builtins.bot_active = True

# ✅ Chạy Flask web app giữ container sống (Railway dùng PORT từ env)
def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# ✅ Chạy lịch trình báo cáo/ngày
def run_scheduler_safe():
    try:
        run_scheduler()
    except Exception as e:
        print("❌ Lỗi scheduler:", e)

# ✅ Chạy Telegram bot + vòng lặp giao dịch song song
async def run_async_tasks():
    try:
        await asyncio.gather(
            start_telegram_bot(),
            smart_trade_loop()
        )
    except Exception as e:
        print("❌ Lỗi async loop:", e)

# ✅ Gộp toàn bộ vào các luồng riêng biệt
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    threading.Thread(target=run_scheduler_safe).start()
    asyncio.run(run_async_tasks())
