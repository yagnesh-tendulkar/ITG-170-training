from sqlalchemy import Column, ForeignKey, Integer, String

from app.models import Base


class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True)

    task_id = Column(Integer, ForeignKey("tasks.id"))

    action = Column(String)