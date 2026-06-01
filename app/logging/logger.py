"""
Centralized logging configuration for the FastAPI application.

Provides a production-ready `app_logger` configuration with both console
and rotating file handlers and a small helper `get_logger()` to retrieve
loggers consistently across the application.
"""
from __future__ import annotations

import logging
import logging.config
from logging import Logger
from pathlib import Path
from typing import Optional, Union


def _ensure_logs_dir() -> Path:
    """
    Ensure the repository-level `logs/` directory exists and return its Path.

    The `logs/` directory is created relative to the project root (two levels
    up from this file: `app/logging/logger.py` -> project root).
    """
    project_root = Path(__file__).resolve().parents[2]
    logs_dir = project_root / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    return logs_dir


def configure_logging(level: Union[int, str] = logging.INFO) -> None:
    """
    Configure structured logging for the application.

    Args:
        level: Logging level to apply to the root logger (e.g., logging.INFO).
    """
    logs_dir = _ensure_logs_dir()
    log_file = str(logs_dir / "app.log")

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s | %(levelname)s | %(module)s | %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "default",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "default",
                "filename": log_file,
                "maxBytes": 10 * 1024 * 1024,  # 10MB
                "backupCount": 5,
                "encoding": "utf-8",
            },
        },
        "root": {
            "level": level,
            "handlers": ["console", "file"],
        },
        "loggers": {
            "app_logger": {"level": level, "handlers": ["console", "file"], "propagate": False},
        },
    }

    logging.config.dictConfig(logging_config)


# Configure logging at import time with sane defaults. Call again to override.
configure_logging()


def get_logger(name: Optional[str] = None) -> Logger:
    """
    Get a configured logger for a given module or component.

    Args:
        name: Optional logger name. If omitted, returns the `app_logger`.

    Returns:
        Logger: Configured logger instance.
    """
    if name:
        return logging.getLogger(name)
    return logging.getLogger("app_logger")


# Expose a module-level logger for convenience
app_logger: Logger = get_logger()


if __name__ == "__main__":
    # Quick self-test
    logger = get_logger("test_module")
    logger.debug("Debug message")
    logger.info("Info message")
    logger.error("Error message")
