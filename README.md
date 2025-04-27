# Algotrader - Real-Time Binance Orderbook Monitoring & Metrics Dashboard

## 🔍 Proje Amacı
- Binance WebSocket kullanarak **gerçek zamanlı** fiyat/volume verisi almak
- SMA-50 / SMA-200 ile **al/sat sinyalleri** üretmek
- **MongoDB** veritabanına orderbook verileri ve sinyaller kaydetmek
- **Prometheus** ile sistem metriklerini toplamak
- **Grafana** ile CPU, RAM, Uptime gibi sistem verilerini izlemek
- **Mongo Express** ile veritabanı verilerini görsel arayüz üzerinden takip etmek

---

## 🔧 Kullanılan Teknolojiler
- Python 3.11 (FastAPI, asyncio, websockets, pymongo, psutil)
- Docker & Docker Compose
- MongoDB
- Mongo Express
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
| FastAPI Healthcheck | [http://localhost:8000/health](http://localhost:8000/health) |
| FastAPI Metrics | [http://localhost:8000/metrics](http://localhost:8000/metrics) |
| Prometheus UI | [http://localhost:9090](http://localhost:9090) |
| Grafana UI | [http://localhost:3000](http://localhost:3000) |
| MongoDB | localhost:27017 |
| Mongo Express | [http://localhost:8081](http://localhost:8081) |

---

## 🔢 Prometheus Ayarları

`prometheus.yml` dosyası şu şekilde yapılandırılmıştır:

```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'algotrader-monitor'
    static_configs:
      - targets: ['algotrader:8000']
```

Bu ayar sayesinde Prometheus, 5 saniyede bir FastAPI `/metrics` endpointinden veri çeker.

---

## 🔹 Grafana Ayarları

Grafana'da yeni bir **Datasource** eklerken:

- **Type**: Prometheus
- **URL**: `http://prometheus:9090` (Container ismiyle)

Önerilen Dashboard panelleri:

- CPU Usage (%)
- Memory Usage (%)
- Uptime (Seconds)
- Total Memory (MB)
- Used Memory (MB)

> ✨ JSON import dosyası istersen ayrıca sağlanabilir.

---

## 🚀 FastAPI `/metrics` Endpointi

FastAPI uygulaması şu verileri sağlamaktadır:

- `uptime_seconds`: Uygulamanın açık kaldığı süre (saniye cinsinden)
- `cpu_percent`: CPU kullanım yüzdesi
- `memory_percent`: RAM kullanım yüzdesi
- `total_memory_mb`: Toplam RAM kapasitesi (MB)
- `used_memory_mb`: Kullanılan RAM miktarı (MB)

Prometheus bu verileri çeker, Grafana ise görüsellerini oluşturur.

---

## 📂 WebSocket Bağlantısı ve Order Manager

- Binance WebSocket ile **gerçek zamanlı** fiyat ve hacim verisi alınır.
- **SMA-50 / SMA-200** hesaplanarak alım-satım sinyalleri üretilir.
- Pozisyonlar açılır ve MongoDB'ye kaydedilir.
- `BUY` / `SELL` sinyalleri console loglarında görülebilir.

---

## 📆 Mongo Express ile MongoDB Takibi

- Mongo Express arayüzü ile MongoDB veritabanındaki koleksiyonlar ve belgeler görüntülenebilir.
- Giriş yapmak gerekmez (authentication devre dışı bırakıldıysa).
- **Adres**: [http://localhost:8081](http://localhost:8081)

---

## ❌ Önemli Notlar

- Container isimleriyle erişim yapılır (hostnames): `algotrader`, `prometheus`, `grafana`, `mongo`, `mongo-express`
- Tarayıcıda `localhost` kullanarak erişim sağlanır.
- Grafana ayarlarının kaybolmaması için volume doğru tanımlandı.

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

