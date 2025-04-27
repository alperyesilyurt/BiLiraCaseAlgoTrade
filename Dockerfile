# Temel Python imajı
FROM python:3.11-slim

# Çalışma dizini oluştur
WORKDIR /app

# Gereksinimleri kopyala
COPY requirements.txt /app/

# Gereksinimleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyala
COPY . /app/

# Docker container başlatıldığında çalışacak komut
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
