from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskCreate(BaseModel):

    title: str

    description: Optional[str] = None


class TaskUpdate(BaseModel):

    title: Optional[str] = None

    description: Optional[str] = None

    status: Optional[str] = None


class TaskResponse(BaseModel):

    id: int

    title: str

    description: str | None

    status: str

    created_at: datetime

    user_id: int

    class Config:
        from_attributes = True