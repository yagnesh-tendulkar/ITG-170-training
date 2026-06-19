from sqlalchemy import Column, Integer, String
from database import Base
class employee(Base):
    __tablename__ = "employees"
    emp_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)