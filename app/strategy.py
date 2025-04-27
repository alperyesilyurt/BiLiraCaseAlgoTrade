from collections import deque
import numpy as np
from datetime import datetime

SMA_SHORT = 50
SMA_LONG = 200

# Fiyatları tutmak için kuyruk
prices = deque(maxlen=SMA_LONG)

# Önceki sinyal (tekrar etmemesi için)
last_signal = None

def calculate_sma(period):
    if len(prices) < period:
        return None
    return np.mean(list(prices)[-period:])

def check_sma_signal(new_price):
    global last_signal
    prices.append(float(new_price))

    sma_short = calculate_sma(SMA_SHORT)
    sma_long = calculate_sma(SMA_LONG)

    if sma_short is None or sma_long is None:
        return None  # Yeterli veri yok

    # Sinyal üretimi
    if sma_short > sma_long and last_signal != "BUY":
        last_signal = "BUY"
        return {
            "signal": "BUY",
            "price": new_price,
            "timestamp": datetime.utcnow().isoformat()
        }

    elif sma_short < sma_long and last_signal != "SELL":
        last_signal = "SELL"
        return {
            "signal": "SELL",
            "price": new_price,
            "timestamp": datetime.utcnow().isoformat()
        }

    return None  # Sinyal yok
