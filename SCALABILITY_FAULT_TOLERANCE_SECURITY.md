# Scalability, Fault Tolerance, and Security Report

## Scalability

- **Containerization with Docker Compose:**  
  Uygulama tüm bileşenleriyle Docker üzerinde containerize edilmiştir. Bu sayede her servis bağımsız olarak yatayda (horizontal scaling) kolayca çoğaltılabilir.
  
- **Lightweight Frameworks:**  
  FastAPI ve WebSocket kullanımı, düşük CPU ve RAM kullanımıyla yüksek yük altında bile performanslı çalışmayı garanti eder.

- **Stateless Application Design:**  
  Ana uygulama (orderbook listener) tamamen stateless çalışacak şekilde tasarlanmıştır. Gerektiğinde yeni instance'lar açılarak yük dağıtılabilir.

- **Monitoring and Alerting:**  
  Prometheus ve Grafana entegrasyonu ile performans ölçümleri gerçek zamanlı olarak izlenebilir. Sistem kaynaklarının tükenmesi gibi durumlar erkenden tespit edilebilir.

## Fault Tolerance

- **Automatic WebSocket Reconnect:**  
  Binance WebSocket bağlantısı koparsa, sistem otomatik olarak 5 saniye sonra yeniden bağlanmayı dener. Böylece network kesintilerine dayanıklıdır.

- **Service Dependency Management:**  
  Docker Compose ile servisler arası bağımlılıklar (`depends_on`) tanımlanmıştır. Böylece MongoDB gibi kritik bileşenler hazır olmadan uygulama başlatılmaz.

- **Database Operation Handling:**  
  MongoDB işlemleri (insert, update) her zaman `try-except` blokları ile güvence altına alınmıştır. Bağlantı hataları sistemin çökmesine neden olmaz, loglanır.

- **Container Restart Policies (Recommended Future Step):**  
  İleride `restart: always` gibi Docker ayarları ile konteynerler crash sonrası otomatik yeniden başlatılacak şekilde ayarlanabilir.

## Security

- **Minimal Network Exposure:**  
  Dış dünyaya sadece gerekli portlar açılmıştır:  
  - Algoritmik trader API (8000)
  - Prometheus (9090)
  - Grafana (3000)
  - MongoDB (27017 - sadece localhost erişimli olarak yapılandırılabilir ileride)

- **Secure Docker Volumes:**  
  MongoDB ve Grafana verileri host makinaya volume olarak yazılmaktadır. Böylece container silinse bile veriler kaybolmaz.

- **Prometheus Scraping:**  
  Sadece belirli bir hedef (`algotrader:8000/metrics`) scrape edilmektedir. Gelişigüzel veri çekimi engellenmiştir.

- **Planned Security Improvements:**  
  - FastAPI uygulamasına HTTPS (TLS) kurulumu yapılabilir.
  - MongoDB'ye kullanıcı/şifre authentication (SCRAM-SHA-1 veya SCRAM-SHA-256) eklenebilir.
  - Docker ağları `internal` yapılarak dış erişim iyice kısıtlanabilir.

## Challenges Faced and Solutions

| Challenge | Solution |
|:----------|:---------|
| WebSocket bağlantısının dockerize ortamda stabil olmaması | `asyncio` ve otomatik reconnect mekanizması geliştirildi. |
| MongoDB container erişimi (`localhost` problemi) | Bağlantı URI'si `mongodb` hostname'i ile güncellendi. |
| Prometheus'un FastAPI endpointinden veri çekememesi | `/metrics` endpointi Prometheus uyumlu text formatında dönecek şekilde yeniden yazıldı. |
| Grafana dashboard ve datasource kaybolması | Grafana container'ı için kalıcı volume (`grafana_data`) eklendi. |
| Dashboard importunda "Datasource not found" hatası | JSON dosyasındaki datasource adı Prometheus ile eşleştirildi. |

---

# Ekstra Öneriler (Deployment için)

- **Container Auto-Restart:**  
  docker-compose.yml dosyasına tüm kritik servisler için:  
  ```yaml
  restart: always
  ```
  eklenebilir. Böylece makine kapanıp açıldığında sistem otomatik ayağa kalkar.

- **Load Balancer ile Ölçekleme:**  
  Traefik veya Nginx gibi bir reverse proxy kullanılarak, çoklu algotrader instance'ları arasında yük dengelenebilir.

- **Security Hardening:**  
  - Grafana login için default şifreler değiştirilmeli.
  - MongoDB'ye yetkilendirme ve IP whitelist uygulanmalı.
  - FastAPI için CORS politikaları sıkılaştırılabilir.
