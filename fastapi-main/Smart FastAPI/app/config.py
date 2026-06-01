import os

class Settings:
    PROJECT_NAME = "Smart Task API"
    API_PREFIX = "/api/v1"

    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWORD = "password"
    DB_NAME = "smart_task_db"

    JWT_SECRET = "123456789098765432123456789098765432123456789q45676543212ertghnjmhtrdfvfrergnjmhg"
    JWT_ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

settings = Settings()