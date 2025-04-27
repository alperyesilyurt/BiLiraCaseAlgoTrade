import logging

# Logger'ı oluştur
logger = logging.getLogger("algotrading")
logger.setLevel(logging.INFO)

# Konsola yazacak handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Log formatı
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
console_handler.setFormatter(formatter)

# Logger'a handler ekle
logger.addHandler(console_handler)
