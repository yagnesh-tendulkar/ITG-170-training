from sqlalchemy import Column, Integer, String
from app.database.database import Base

class ComplaintLog(Base):
    __tablename__ = "complaint_logs"

    id = Column(Integer, primary_key=True, index=True)
    complaint_id = Column(Integer)
    message = Column(String)