from pydantic import (
    BaseModel,
    field_validator,
    model_validator,
)

from typing import Optional
from datetime import datetime, timezone


class TaskCreate(BaseModel):

    title: str
    description: str
    priority: str
    due_date: datetime

    @field_validator("priority")
    def validate_priority(cls, value):

        allowed = [
            "low",
            "medium",
            "high"
        ]

        if value.lower() not in allowed:
            raise ValueError(
                "Priority must be low, medium or high"
            )

        return value.lower()

    @model_validator(mode="after")
    def validate_due_date(self):
        due = self.due_date
        if due.tzinfo is None:
            due = due.replace(tzinfo=timezone.utc)

        now = datetime.now(timezone.utc)

        if due < now:
            raise ValueError(
                "Due date cannot be in the past"
            )

        return self


class TaskUpdate(BaseModel):

    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    due_date: Optional[datetime] = None


class ChatRequest(BaseModel):
    prompt: str
    max_tokens: Optional[int] = 200
