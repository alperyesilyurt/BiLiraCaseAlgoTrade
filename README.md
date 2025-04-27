# Algotrader - Real-Time Binance Orderbook Monitoring & Metrics Dashboard

## 🔍 Proje Amacı
- Binance WebSocket kullanarak **gerçek zamanlı** fiyat/volume verisi almak
- SMA-50 / SMA-200 ile **al/sat sinyalleri** üretmek
- **MongoDB** veritabanına orderbook verileri ve sinyaller kaydetmek
- **Prometheus** ile sistem metriklerini toplamak
- **Grafana** ile CPU, RAM, Uptime gibi sistem verilerini izlemek

---

## 🔧 Kullanılan Teknolojiler
- Python 3.11 (FastAPI, asyncio, websockets, pymongo, psutil)
- Docker & Docker Compose
- MongoDB
- Prometheus
- Grafana

---

## 📁 Proje Yapısı

```bash
algotrader/
├── app/
│   ├── config.py
│   ├── database.py
│   ├── order_manager.py
│   ├── streamer.py
│   └── strategy.py
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml
├── requirements.txt
└── main.py
```

---

## 🔄 Kurulum Adımları

1. **Repository'i klonla:**
```bash
git clone <repo-link>
cd algotrader
```

2. **Docker imajlarını oluştur ve containerları başlat:**
```bash
docker compose up --build
```

---

## 🔗 Hizmetler

| Hizmet | Adres |
|:---|:---|
| FastAPI Healthcheck | http://localhost:8000/health |
| FastAPI Metrics | http://localhost:8000/metrics |
| Prometheus UI | http://localhost:9090 |
| Grafana UI | http://localhost:3000 |
| MongoDB | localhost:27017 |

---

## 🔢 Prometheus Ayarları

`prometheus.yml` dosyası şöyle ayarlı:
```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'algotrader-monitor'
    static_configs:
      - targets: ['algotrader:8000']
```
Bu sayede Prometheus, 5 saniyede bir `/metrics` endpointinden veri çeker.

---

## 🔹 Grafana Ayarları

**Datasource** eklerken:
- Type: **Prometheus**
- URL: **http://prometheus:9090** (Dışarıdan değil container adıyla)

**Dashboard** için panel örnekleri:
- CPU Usage (%)
- Memory Usage (%)
- Uptime (Seconds)
- Total Memory (MB)
- Used Memory (MB)

> ✨ JSON import önerisi istersen dosya ayrıca verilebilir.

---

## 🚀 FastAPI `/metrics` endpointi ne veri sağlıyor?
- `uptime_seconds`: Uygulamanın açık kaldığı süre
- `cpu_percent`: CPU kullanım yüzdesi
- `memory_percent`: RAM kullanım yüzdesi
- `total_memory_mb`: Toplam RAM (MB)
- `used_memory_mb`: Kullanılan RAM (MB)

Prometheus bu verileri çeker, Grafana ise görüsellerini oluşturur.

---

## 🔹 WebSocket Bağlantısı ve Order Manager
- Binance WebSocket ile **real-time** fiyat ve hacim verisi alınıyor.
- **SMA-50 / SMA-200** hesaplanarak alım-satım sinyalleri üretiliyor.
- Pozisyonlar açılıyor ve MongoDB'ye kaydediliyor.
- `BUY`/`SELL` sinyalleri console loglarında görülebilir.

---

## 🚫 Önemli Notlar
- Container isimleriyle erişim yapılıyor (hostnames): `algotrader`, `prometheus`, `grafana`
- Tarayıcıda `localhost` kullanarak erişim sağlanır.
- Grafana ayarları veya dashboardları kaybolmaması için volume doğru tanımlandı.

---

## 🌟 Katkı
Pull request veya issue açarak katkıda bulunabilirsiniz.
Her türlü iyileştirme ve öneriye açığız!

---

## 📚 Lisans
Bu proje öğrenme ve gösterim amaçlıdır.
Ticari kullanım için geliştirilmemiştir.

---

# 🔥 Haydi Trading Bot'unu izlemeye başlayalım!

