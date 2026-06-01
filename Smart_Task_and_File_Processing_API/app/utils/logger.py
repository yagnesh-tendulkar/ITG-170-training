import logging
from logging.handlers import RotatingFileHandler
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Create logger object
logger = logging.getLogger("smart_task_api")

# Set minimum log level
logger.setLevel(logging.INFO)

# Prevent duplicate logs
logger.propagate = False

# Log format
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# File Handler
file_handler = RotatingFileHandler(
    filename="logs/app.log",
    maxBytes=1024 * 1024,  # 1 MB
    backupCount=5
)

file_handler.setFormatter(formatter)

# Add handlers only once
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)