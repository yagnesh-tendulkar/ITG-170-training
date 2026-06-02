from sqlalchemy import Column, ForeignKey, Integer, String, Text

from app.models import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(Text)

    status = Column(String, default="pending")

    priority = Column(String, default="medium")

    owner_id = Column(Integer, ForeignKey("users.id"))