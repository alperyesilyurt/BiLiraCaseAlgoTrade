from pymongo import MongoClient
from app.config import MONGO_URI, DB_NAME, ORDERBOOK_COLLECTION, SIGNAL_COLLECTION, ORDER_COLLECTION
from app.logger import logger

class MongoDBClient:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DB_NAME]
        self.orderbook_collection = self.db[ORDERBOOK_COLLECTION]
        self.signal_collection = self.db[SIGNAL_COLLECTION]

    def insert_orderbook(self, data: dict):
            try:
                self.orderbook_collection.insert_one(data)
            except Exception as e:
                logger.error(f"[MongoDB] Error inserting orderbook data: {e}")

    def insert_signal(self, signal: dict):
        try:
            self.signal_collection.insert_one(signal)
        except Exception as e:
            logger.error(f"[MongoDB] Error inserting signal data: {e}")

    def insert_order(self, order: dict):
        try:
            self.db[ORDER_COLLECTION].insert_one(order)
        except Exception as e:
            logger.error(f"[MongoDB] Error inserting order: {e}")

    def update_order_status(self, original_order: dict, updated_order: dict):
        try:
            self.db[ORDER_COLLECTION].update_one(
                {"entry_price": original_order["entry_price"], "opened_at": original_order["opened_at"]},
                {"$set": updated_order}
            )
        except Exception as e:
            logger.error(f"[MongoDB] Error updating order status: {e}")
        try:
            self.db[ORDER_COLLECTION].update_one(
                {
                    "entry_price": original_order["entry_price"],
                    "opened_at": original_order["opened_at"]
                },
                {"$set": updated_order}
            )
        except Exception as e:
            print(f"[MongoDB] Error updating order status: {e}")

