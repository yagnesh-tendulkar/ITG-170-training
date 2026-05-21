from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url = "mysql+pymysql://root:M1racle%40123@localhost/employeedb"
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
