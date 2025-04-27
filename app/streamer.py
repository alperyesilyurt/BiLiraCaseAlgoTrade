import asyncio
import json
import websockets
from datetime import datetime

from app.config import BINANCE_WS_URL
from app.database import MongoDBClient
from app.strategy import check_sma_signal
from app.order_manager import open_order
from app.logger import logger

db_client = MongoDBClient()

MAX_RETRIES = 10
RETRY_DELAY = 5 

async def listen_to_orderbook():
    retry_count = 0

    while retry_count < MAX_RETRIES:
        try:
            async with websockets.connect(BINANCE_WS_URL, ping_interval=20, ping_timeout=20) as websocket:
                logger.info("[WebSocket] Connected to Binance ✅")
                retry_count = 0

                while True:
                    message = await websocket.recv()
                    data = json.loads(message)

                    logger.info(f"[Data] Price: {data.get('p')}, Quantity: {data.get('q')}")

                    data['received_at'] = datetime.utcnow().isoformat()
                    db_client.insert_orderbook(data)

                    signal = check_sma_signal(data.get("p"))
                    if signal:
                        logger.info(f"[SIGNAL] {signal['signal']} at {signal['price']}")
                        db_client.insert_signal(signal)
                        open_order(signal)

        except (websockets.ConnectionClosedError, websockets.InvalidStatusCode, ConnectionResetError) as e:
            retry_count += 1
            logger.error(f"[WebSocket] Connection error: {e}. Retry {retry_count}/{MAX_RETRIES} in {RETRY_DELAY} seconds...")
            await asyncio.sleep(RETRY_DELAY)

        except Exception as e:
            logger.error(f"[WebSocket] Unexpected error: {e}. Retry {retry_count}/{MAX_RETRIES} in {RETRY_DELAY} seconds...")
            retry_count += 1
            await asyncio.sleep(RETRY_DELAY)

    logger.error("[WebSocket] Max retries reached. Exiting...")