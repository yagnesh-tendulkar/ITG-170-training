# app/__init__.py

"""
HR Employee Portal
A FastAPI-based HR Management System
"""

__version__ = "1.0.0"

# Optional: You can expose main components here for cleaner imports
from .main import app
from .database import get_db, engine, Base

__all__ = ["app", "get_db", "engine", "Base"]