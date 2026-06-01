from sqlmodel import SQLModel, create_engine, Session

from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

load_dotenv()
password=quote_plus((os.getenv('DB_PASSWORD')))
DATABASE_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{password}@localhost:3306/{os.getenv('DB')}"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session