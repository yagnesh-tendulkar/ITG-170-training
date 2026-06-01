from datetime import datetime

from sqlalchemy import column, Integer, String, Boolean, DateTime, Column
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    name=Column(String(100),nullable =True)
    email = Column(String(150),unique=True,nullable=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime(timezone = True),server_default = func.now())
    updated_at = Column(DateTime(timezone = True),onupdate=func.now())
