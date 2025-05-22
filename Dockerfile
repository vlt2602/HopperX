# Sử dụng bản đầy đủ Debian để build an toàn
FROM python:3.10-bullseye

# Thiết lập thư mục làm việc
WORKDIR /app

# Cài pip mới + hỗ trợ build
RUN pip install --upgrade pip setuptools wheel

# Sao chép mã nguồn vào container
COPY . .

# Cài đặt thư viện yêu cầu
RUN pip install --no-cache-dir -r requirements.txt

# Mở cổng Flask
EXPOSE 5000

# Chạy ứng dụng
CMD ["python", "flask_app.py"]
