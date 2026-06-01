from enum import Enum

from pydantic import BaseModel


class TaskStatus(str, Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


class TaskCreate(BaseModel):

    title: str
    description: str


class TaskUpdate(BaseModel):

    title: str
    description: str
    status: TaskStatus


class TaskResponse(BaseModel):

    id: int
    title: str
    description: str
    status: str

    class Config:
        from_attributes = True