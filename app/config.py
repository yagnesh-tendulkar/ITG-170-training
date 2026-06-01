from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY`", "supersecretkey")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:M1racle%40123@localhost:3306/smart_task_db"
)