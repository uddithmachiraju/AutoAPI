# logger.py
import logging
import os

LOG_BASE_DIR = "logs"
APP_START_TIME = os.environ.get("LOG_START_TIME", "default")
LOG_DIR = os.path.join(LOG_BASE_DIR, APP_START_TIME)
os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(log_name, level): 
    log_filename = os.path.join(LOG_DIR, f"{log_name}.log") 

    logger = logging.getLogger(log_name)
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logger.setLevel(numeric_level)
    
    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_filename, mode='a') 
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False
    return logger
