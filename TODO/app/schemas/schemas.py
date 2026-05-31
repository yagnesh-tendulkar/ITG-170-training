from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, computed_field
from typing import Optional, List
from datetime import datetime, timezone

# --- USER SCHEMAS ---
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


# --- TASK SCHEMAS ---
class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    priority: str = Field("medium", pattern="^(low|medium|high)$")
    status: str = Field("pending", pattern="^(pending|completed)$")
    due_date: Optional[datetime] = None

    # Modern Input Validator using standard timezone-aware datetime
    @model_validator(mode="after")
    def validate_due_date_input(self) -> 'TaskBase':
        if self.due_date:
            # Force target due_date to be timezone aware if it isn't
            due_date_aware = self.due_date if self.due_date.tzinfo else self.due_date.replace(tzinfo=timezone.utc)
            now_aware = datetime.now(timezone.utc)
            
            if due_date_aware < now_aware:
                raise ValueError("Due date cannot be set in the past.")
        return self


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    due_date: Optional[datetime] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    priority: str
    status: str
    due_date: Optional[datetime] = None
    user_id: int
    created_at: datetime
    file_attachment: Optional[str] = None

    @field_validator("title")
    @classmethod
    def title_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Title cannot be an empty space string.")
        return value

    # Modern Computed Field using timezone-aware calculations
    @computed_field
    @property
    def is_overdue(self) -> bool:
        if self.due_date and self.status != "completed":
            due_date_aware = self.due_date if self.due_date.tzinfo else self.due_date.replace(tzinfo=timezone.utc)
            return datetime.now(timezone.utc) > due_date_aware
        return False

    class Config:
        from_attributes = True