from urllib.parse import quote_plus
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()


password = quote_plus(
    os.getenv("DB_PASSWORD","")
)

DATABASE_URL = (
    f"mysql+pymysql://"
    f"{os.getenv('DB_USER')}:"
    f"{password}@"
    f"{os.getenv('DB_HOST')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(
    DATABASE_URL,
    echo=True
)
print(os.getenv("DB_PASSWORD"))
print("DATABASE_URL =", DATABASE_URL)