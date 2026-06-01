from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title:       str
    description: Optional[str] = None
    priority:    Optional[str] = "medium"
    user_id:     Optional[int] = None

class TaskUpdate(BaseModel):
    title:       Optional[str]  = None
    description: Optional[str]  = None
    completed:   Optional[bool] = None
    priority:    Optional[str]  = None

class TaskResponse(BaseModel):
    id:          int
    title:       str
    description: Optional[str]
    completed:   bool
    priority:    str
    user_id:     Optional[int]
    created_at:  Optional[datetime]

    class Config:
        from_attributes = True