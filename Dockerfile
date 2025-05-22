# Sử dụng hình ảnh Python chính thức
FROM python:3.10-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Cài pip mới + hỗ trợ biên dịch tốt hơn
RUN pip install --upgrade pip setuptools wheel

# Sao chép mã nguồn vào container
COPY . .

# Cài đặt thư viện yêu cầu
RUN pip install --no-cache-dir -r requirements.txt

# Mở cổng Flask (mặc định 5000)
EXPOSE 5000

# Chạy ứng dụng
CMD ["python", "flask_app.py"]
