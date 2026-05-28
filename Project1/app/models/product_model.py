from sqlalchemy import column, Column
from sqlalchemy import String
from sqlalchemy import Integer
from app.database.connection import Base
class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index = True)
    name = Column(String(100),nullable=False)
    price = Column(Integer,nullable=False)
    quantity = Column(Integer,nullable=False)
    
