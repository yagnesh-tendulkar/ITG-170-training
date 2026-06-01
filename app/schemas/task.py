from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional

from pydantic import (
    BaseModel,
    computed_field,
    field_validator,
)


class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class StatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: PriorityEnum = PriorityEnum.medium
    tags: List[str] = []
    due_date: Optional[datetime] = None

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        value = value.strip()

        if len(value) < 3:
            raise ValueError(
                "Title must be at least 3 characters"
            )

        return value

    @field_validator("due_date")
    @classmethod
    def validate_due_date(
        cls,
        value: Optional[datetime],
    ) -> Optional[datetime]:

        if value is None:
            return value

        # Convert naive datetime to timezone-aware UTC
        if value.tzinfo is None:
            value = value.replace(
                tzinfo=timezone.utc
            )

        if value < datetime.now(timezone.utc):
            raise ValueError(
                "Due date cannot be in the past"
            )

        return value


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusEnum] = None
    priority: Optional[PriorityEnum] = None
    tags: Optional[List[str]] = None
    due_date: Optional[datetime] = None

    @field_validator("title")
    @classmethod
    def validate_title(
        cls,
        value: Optional[str],
    ) -> Optional[str]:

        if value is None:
            return value

        value = value.strip()

        if len(value) < 3:
            raise ValueError(
                "Title must be at least 3 characters"
            )

        return value

    @field_validator("due_date")
    @classmethod
    def validate_due_date(
        cls,
        value: Optional[datetime],
    ) -> Optional[datetime]:

        if value is None:
            return value

        # Convert naive datetime to timezone-aware UTC
        if value.tzinfo is None:
            value = value.replace(
                tzinfo=timezone.utc
            )

        if value < datetime.now(timezone.utc):
            raise ValueError(
                "Due date cannot be in the past"
            )

        return value


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: StatusEnum
    priority: PriorityEnum
    tags: List[str]
    file_path: Optional[str] = None
    owner_id: int
    due_date: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    @computed_field
    @property
    def is_overdue(self) -> bool:

        if self.due_date is None:
            return False

        due_date = self.due_date

        # Convert naive datetime to timezone-aware UTC
        if due_date.tzinfo is None:
            due_date = due_date.replace(
                tzinfo=timezone.utc
            )

        return (
            due_date < datetime.now(timezone.utc)
            and self.status != StatusEnum.completed
        )

    model_config = {
        "from_attributes": True
    }


class TaskFilter(BaseModel):
    status: Optional[StatusEnum] = None
    priority: Optional[PriorityEnum] = None
    search: Optional[str] = None

    page: int = 1
    limit: int = 10

    sort_by: str = "created_at"
    order: str = "desc"

    @field_validator("page")
    @classmethod
    def validate_page(cls, value: int) -> int:

        if value < 1:
            raise ValueError(
                "Page must be greater than 0"
            )

        return value

    @field_validator("limit")
    @classmethod
    def validate_limit(cls, value: int) -> int:

        if value < 1 or value > 100:
            raise ValueError(
                "Limit must be between 1 and 100"
            )

        return value

    @field_validator("order")
    @classmethod
    def validate_order(cls, value: str) -> str:

        allowed_orders = {"asc", "desc"}

        if value not in allowed_orders:
            raise ValueError(
                "Order must be 'asc' or 'desc'"
            )

        return value

    @field_validator("sort_by")
    @classmethod
    def validate_sort_by(
        cls,
        value: str,
    ) -> str:

        allowed_fields = {
            "created_at",
            "updated_at",
            "due_date",
            "priority",
            "title",
            "status",
        }

        if value not in allowed_fields:
            raise ValueError(
                f"sort_by must be one of: "
                f"{', '.join(allowed_fields)}"
            )

        return value