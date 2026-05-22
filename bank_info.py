from sqlalchemy import Column, Integer, String
from database import Base

class BankUser(Base):
    __tablename__ = "bank_users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    account_no = Column(String)
    balance = Column(Integer)