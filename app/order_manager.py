from datetime import datetime
from app.database import MongoDBClient
from app.logger import logger


db = MongoDBClient()
active_order = None  # global gibi davranacak, sadece 1 pozisyon açık tutulacak

def open_order(signal: dict):
    global active_order

    # Zaten açık pozisyon varsa ters sinyal gelene kadar bir şey yapma
    if active_order and active_order['signal'] == signal['signal']:
        return None

    # Mevcut pozisyon varsa, kapat
    if active_order:
        close_order(active_order)

    # Yeni pozisyon oluştur
    order = {
        "type": "MARKET",
        "signal": signal["signal"],
        "entry_price": signal["price"],
        "status": "OPEN",
        "opened_at": signal["timestamp"]
    }

    db.insert_order(order)
    active_order = order
    logger.info(f"[ORDER] Opened {order['signal']} at {order['entry_price']}")

    return order

def close_order(order: dict):
    global active_order

    closed_order = order.copy()
    closed_order["status"] = "CLOSED"
    closed_order["closed_at"] = datetime.utcnow().isoformat()

    db.update_order_status(order, closed_order) 
    logger.info(f"[ORDER] Closed {order['signal']} from {order['entry_price']}")
    active_order = None
