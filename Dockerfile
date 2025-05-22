# Sử dụng hình ảnh Python chính thức
FROM python:3.10-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép mã nguồn vào container
COPY . .

# Cài đặt thư viện yêu cầu
RUN pip install --no-cache-dir -r requirements.txt

# Mở cổng Flask (mặc định 5000)
EXPOSE 5000

# Chạy ứng dụng
CMD ["python", "flask_app.py"]
