from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(String, default="OPEN")
    priority = Column(String, default="MEDIUM")