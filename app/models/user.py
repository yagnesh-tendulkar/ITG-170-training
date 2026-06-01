from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)              # user full name
    email = Column(String(255), unique=True, index=True, nullable=False)  # email
    hashed_password = Column(String(255), nullable=False)   # hashed passwords are fixed size-ish

    age = Column(Integer, nullable=False)

    is_active = Column(Boolean, default=True)

    api_key = Column(String(64), unique=True, nullable=True)  # API keys usually fixed length

    created_at = Column(DateTime, default=datetime.utcnow)

    tasks = relationship(
        "Task",
        back_populates="owner",
        cascade="all, delete"
    )