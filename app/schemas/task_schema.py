from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
    computed_field,
)
from typing import List, Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title : str 
    description : str
    priority : str
    tags : List[str]
    created_at: datetime = datetime.utcnow()
    due_date: datetime

    @field_validator("priority")
    def validate_priority(cls, value):
        allowed = ["low","high","medium"]

        if value not in allowed:
            raise ValueError(
                "Priority must be low, medium, high"
            )
        return value

    @model_validator(mode="after")
    def validate_due_date(self):

        if self.due_date < self.created_at:
            raise ValueError(
                "Due date cannot be before created date"
            )

        return self

    @computed_field
    @property
    def is_overdue(self) -> bool:

        return self.due_date < datetime.utcnow()


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description : Optional[str] = None
    priority : Optional[str] = None
    tags : Optional[List[str]] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str   
    tags: List[str]
