import os

# --- Binance ---
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET = os.getenv("BINANCE_API_SECRET")

# --- Telegram ---
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID", "0"))
ALLOWED_CHAT_ID = TELEGRAM_CHAT_ID  # Cùng 1 giá trị để hạn chế người lạ

# --- Giao dịch ---
TRADE_SYMBOLS = ["ETH/USDT", "BTC/USDT"]
TRADE_PERCENT = 0.05  # fallback nếu không dùng vốn cố định

# --- Vốn cố định ---
USE_FIXED_CAPITAL = True
FIXED_USDT_PER_ORDER = 15

# --- Giới hạn vốn đầu tư ---
USE_CAPITAL_LIMIT = True
CAPITAL_LIMIT = 500  # USDT giới hạn đầu tư

# --- Ghi log Google Sheet ---
USE_GOOGLE_SHEET = False
SHEET_WEBHOOK = os.getenv("SHEET_WEBHOOK", "")

# --- Giới hạn lỗ trong ngày ---
DAILY_MAX_LOSS = -30  # cho phép lỗ tối đa 30 USDT/ngày
