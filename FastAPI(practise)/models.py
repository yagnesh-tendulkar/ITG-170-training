from sqlalchemy import Column, Integer, String
from database import Base   # ✅ correct

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)