from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import builtins
import pandas as pd
from strategy_metrics import get_strategy_scores
from balance_helper import get_balance, get_used_capital
from config import ALLOWED_CHAT_ID

# ... giữ nguyên các hàm status, resume, capital,... của anh như trước

# ✅ Khởi động Telegram Bot
async def start_telegram_bot():
    app = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    # Đăng ký command handler
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

    print("✅ Telegram bot đã khởi động (v20+)")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await app.updater.wait_for_stop()
