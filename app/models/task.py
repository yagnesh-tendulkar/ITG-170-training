from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)          # short text
    description = Column(String(1000), nullable=True)    # longer text

    status = Column(String(20), default="pending")       # pending | in_progress | completed
    priority = Column(String(20), default="medium")      # low | medium | high

    tags = Column(JSON, default=list)

    file_path = Column(String(500), nullable=True)       # file path can be long

    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    due_date = Column(DateTime, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    owner = relationship("User", back_populates="tasks")
