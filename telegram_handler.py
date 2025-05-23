from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import builtins
import pandas as pd
from strategy_metrics import get_strategy_scores
from balance_helper import get_balance, get_used_capital
from config import ALLOWED_CHAT_ID, TELEGRAM_TOKEN

# ✅ Khởi tạo biến toàn cục
builtins.panic_mode = False
builtins.loss_streak = 0
builtins.capital_limit = 500
builtins.capital_limit_init = 500
builtins.bot_active = True
builtins.last_order = None

# Các hàm lệnh như status, resume, toggle,... giữ nguyên
# Em không gửi lại nội dung hàm để tránh lặp lại, vì logic vẫn như anh đã dùng.

# ✅ Tạo danh sách lệnh
def get_command_handlers():
    return [
        CommandHandler("status", status),
        CommandHandler("resume", resume),
        CommandHandler("toggle", toggle),
        CommandHandler("setcapital", setcapital),
        CommandHandler("capital", capital),
        CommandHandler("strategy", strategy),
        CommandHandler("lastorder", lastorder),
        CommandHandler("report", report),
        CommandHandler("addcapital", addcapital),
        CommandHandler("removecapital", removecapital),
        CommandHandler("resetcapital", resetcapital),
        CommandHandler("menu", menu),
        CommandHandler("top", top),
        CommandHandler("resetlog", resetlog),
        CommandHandler("pause", pause),
    ]

# ✅ Hàm khởi động bot chuẩn v20
async def start_telegram_bot():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    for handler in get_command_handlers():
        application.add_handler(handler)

    print("🚀 Telegram bot đã khởi động – V20 polling...")
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    await application.updater.idle()
