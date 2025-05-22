from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TELEGRAM_TOKEN, ALLOWED_CHAT_ID
import builtins
from strategy_metrics import get_strategy_scores
from balance_helper import get_balance, get_used_capital
import pandas as pd

# ====== Biến toàn cục ======
builtins.panic_mode = False
builtins.loss_streak = 0
builtins.capital_limit = 500
builtins.capital_limit_init = 500
builtins.bot_active = True
builtins.last_order = None

# ====== Các handler như anh đã có (giữ nguyên) ======
# (không lặp lại ở đây để tránh quá dài – code anh chuẩn)

# ====== KHỞI ĐỘNG BOT ======
async def start_telegram_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

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

    print("✅ Telegram bot khởi động...")

    # Dùng run_polling (phiên bản chính thức của v20+)
    await app.run_polling()
