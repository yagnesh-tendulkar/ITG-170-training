from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # DATABASE CONFIG
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "root"
    DB_PASSWORD: str = "M1raclae@123"
    DB_NAME: str = "fastapi"

    # JWT CONFIG
    SECRET_KEY: str = "supersecretkey123asdffffhbkjhgfdsjhgvfcdxzdddffd"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # APP CONFIG
    APP_NAME: str = "Smart Task API"
    DEBUG: bool = True

    class Config:
        env_file = ".env"


settings = Settings()