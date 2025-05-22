from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ HopperX đang chạy!"

@app.route('/healthcheck')
def healthcheck():
    return "✅ HopperX vẫn sống!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Railway sẽ tự động set PORT
    app.run(host='0.0.0.0', port=port)
