# app/core/config.py

class Settings:
    PROJECT_NAME: str = "Book Inventory API"
    PROJECT_VERSION: str = "1.0.0"
    
    ALLOWED_ORIGINS: list[str] = ["*"]

settings = Settings()