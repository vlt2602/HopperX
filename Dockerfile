FROM python:3.10-bullseye

WORKDIR /app

# Cài pip và công cụ build
RUN pip install --upgrade pip setuptools wheel

COPY . .

# Cài từng thư viện riêng để xác định lỗi cụ thể
RUN pip install flask
RUN pip install python-binance
RUN pip install python-telegram-bot==13.15
RUN pip install apscheduler
RUN pip install pandas
RUN pip install numpy
RUN pip install requests
RUN pip install nest_asyncio

EXPOSE 5000

CMD ["python", "flask_app.py"]
