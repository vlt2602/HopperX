from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TELEGRAM_TOKEN, ALLOWED_CHAT_ID
import builtins
import pandas as pd
from strategy_metrics import get_strategy_scores
from balance_helper import get_balance, get_used_capital

# ✅ Khởi tạo biến toàn cục
builtins.panic_mode = False
builtins.loss_streak = 0
builtins.capital_limit = 500
builtins.capital_limit_init = 500
builtins.bot_active = True
builtins.last_order = None

# (giữ nguyên các hàm status, resume, capital,... như anh có)

# ✅ KHỞI ĐỘNG BOT
async def start_telegram_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Đăng ký lệnh
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

    print("🚀 Telegram bot đã khởi động - Đang polling...")

    await app.run_polling()
