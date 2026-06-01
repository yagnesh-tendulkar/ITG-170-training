from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):

    # Application Settings
    APP_NAME: str = "Smart Task API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = (
        "Production Ready FastAPI Project"
    )

    # Database Settings
    DATABASE_URL: str = (
        "mysql+pymysql://root:M1racle%40123@localhost/smart_task_db"
    )

    # JWT Settings
    SECRET_KEY: str = (
        "your_super_secret_key"
    )

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # File Upload Settings
    UPLOAD_DIRECTORY: str = "uploads"

    MAX_FILE_SIZE: int = (
        5 * 1024 * 1024
    )  # 5 MB

    # Logging
    LOG_LEVEL: str = "INFO"

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()