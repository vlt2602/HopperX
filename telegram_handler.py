from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import builtins
import pandas as pd
from strategy_metrics import get_strategy_scores
from balance_helper import get_balance, get_used_capital
from config import ALLOWED_CHAT_ID
import os

# ✅ Các hàm xử lý lệnh Telegram (như đã có: status, resume,...)
# ✅ Toàn bộ phần này sẽ được em dán vào sau khi confirm lại nếu anh muốn

# ✅ Hàm khởi động bot
async def start_telegram_bot():
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("resume", resume))
    app.add_handler(CommandHandler("toggle", toggle))
    app.add_handler(CommandHandler("setcapital", setcapital))
    app.add_handler(CommandHandler("capital", capital))
    app.add_handler(CommandHandler("strategy", strategy))
    app.add_handler(CommandHandler("lastorder", lastorder))
    app.add_handler(CommandHandler("report", report))
    app.add_handler(CommandHandler("addcapital", addcapital))
    app.add_handler(CommandHandler("removecapital", removecapital))
    app.add_handler(CommandHandler("resetcapital", resetcapital))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("top", top))
    app.add_handler(CommandHandler("resetlog", resetlog))
    app.add_handler(CommandHandler("pause", pause))

    print("🚀 Telegram bot đã khởi động – Đang polling...")
    await app.run_polling()
