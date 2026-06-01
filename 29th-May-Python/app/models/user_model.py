from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from .task_model import Task

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    age: int

    tasks: List[Task] = Relationship(back_populates="user")