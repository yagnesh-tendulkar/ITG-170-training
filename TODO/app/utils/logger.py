import logging
import sys
from logging.handlers import RotatingFileHandler
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Define clean log message format
LOG_FORMAT = "%(asctime)s - %(levelname)s - [Request-ID: %(request_id)s] - %(message)s"

class RequestIdFilter(logging.Filter):
    """
    Ensures 'request_id' attribute always exists in the log record, 
    even if log is called outside an HTTP request scope.
    """
    def filter(self, record):
        if not hasattr(record, "request_id"):
            record.request_id = "SYSTEM"
        return True

def setup_logger():
    logger = logging.getLogger("todo_app")
    logger.setLevel(logging.INFO)
    
    # Prevent duplicate handlers if logger initialized multiple times
    if logger.handlers:
        return logger

    formatter = logging.Formatter(LOG_FORMAT)
    request_filter = RequestIdFilter()

    # 1. Console Handler (for real-time container log streaming)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.addFilter(request_filter)
    logger.addHandler(console_handler)

    # 2. File Handler with Rotation (Prevents disk-space exhaustion)
    file_handler = RotatingFileHandler(
        "logs/app.log", maxBytes=5 * 1024 * 1024, backupCount=3
    )
    file_handler.setFormatter(formatter)
    file_handler.addFilter(request_filter)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()