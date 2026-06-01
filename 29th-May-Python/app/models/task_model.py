from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from .user_model import User


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    title: str
    description: str
    status: str = "pending"  # pending, completed, in-progress
    priority: str = "medium"  # low, medium, high
    tags: Optional[str] = None  # store as comma-separated tags

    created_at: datetime = Field(default_factory=datetime.utcnow)
    due_date: Optional[datetime] = None

    user_id: int = Field(foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="tasks")