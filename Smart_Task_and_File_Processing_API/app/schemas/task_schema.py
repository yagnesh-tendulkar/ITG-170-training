from datetime import datetime
from typing import Optional

from pydantic import (
    BaseModel,
    Field,
    field_validator,
    computed_field
)


class TaskCreate(BaseModel):

    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Task Title"
    )

    description: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="Task Description"
    )

    priority: str = Field(
        ...,
        description="Task Priority"
    )

    due_date: Optional[datetime] = None

    @field_validator("priority")
    @classmethod
    def validate_priority(
        cls,
        value: str
    ):

        allowed_priorities = [
            "low",
            "medium",
            "high"
        ]

        if value.lower() not in allowed_priorities:

            raise ValueError(
                "Priority must be low, medium, or high"
            )

        return value.lower()


class TaskUpdate(BaseModel):

    title: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=100
    )

    description: Optional[str] = Field(
        default=None,
        min_length=5,
        max_length=500
    )

    priority: Optional[str] = None

    due_date: Optional[datetime] = None

    @field_validator("priority")
    @classmethod
    def validate_priority(
        cls,
        value
    ):

        if value is None:
            return value

        allowed_priorities = [
            "low",
            "medium",
            "high"
        ]

        if value.lower() not in allowed_priorities:

            raise ValueError(
                "Priority must be low, medium, or high"
            )

        return value.lower()


class TaskResponse(BaseModel):

    id: int

    title: str

    description: str

    priority: str

    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )

    due_date: Optional[datetime] = None

    @computed_field
    @property
    def is_overdue(
        self
    ) -> bool:

        if self.due_date is None:
            return False

        return self.due_date < datetime.utcnow()


class TaskFilter(BaseModel):

    priority: Optional[str] = None

    page: int = Field(
        default=1,
        ge=1
    )

    limit: int = Field(
        default=10,
        ge=1,
        le=100
    )

    search: Optional[str] = None