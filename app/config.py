import os

# Binance WebSocket URL for BTC/USDT (depth stream)
BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"

# MongoDB bağlantı URI'si (localhost)
MONGO_URI = "mongodb://mongodb:27017"

# MongoDB veritabanı ve koleksiyon isimleri
DB_NAME = "algotrading"
ORDERBOOK_COLLECTION = "orderbook_data"
SIGNAL_COLLECTION = "signals"
ORDER_COLLECTION = "orders"
