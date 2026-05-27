from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "mysql+pymysql://root:M1racle%40123@localhost:3306/mydb"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
