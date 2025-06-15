import logging
import os
import datetime

# Create a directory for each run based on the current date and time
log_base_dir = "logs"
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_dir = os.path.join(log_base_dir, timestamp)

os.makedirs(log_dir, exist_ok = True) 

def get_logger(log_name, level): 
    """
    Creates a logger that logs to a file inside a time-stamped directory.
    """
    log_filename = os.path.join(log_dir, f"{log_name}.log") 

    logger = logging.getLogger(log_name)
    # Set the log level dynamically
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logger.setLevel(numeric_level)
    
    # Remove any existing handlers to prevent duplication
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler
    file_handler = logging.FileHandler(log_filename, mode='a') 
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Disable propagation to avoid logs appearing twice
    logger.propagate = False

    return logger
