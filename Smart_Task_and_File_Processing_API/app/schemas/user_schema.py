from datetime import datetime
from typing import Optional

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    field_validator,
    computed_field
)


class UserCreate(BaseModel):

    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="User Full Name"
    )

    email: EmailStr

    age: int = Field(
        ...,
        ge=18,
        le=100,
        description="User Age"
    )

    password: str = Field(
        ...,
        min_length=6,
        max_length=100
    )

    @field_validator("password")
    @classmethod
    def validate_password(
        cls,
        value: str
    ):

        if not any(
            char.isupper()
            for char in value
        ):
            raise ValueError(
                "Password must contain at least one uppercase letter"
            )

        if not any(
            char.isdigit()
            for char in value
        ):
            raise ValueError(
                "Password must contain at least one digit"
            )

        return value


class UserUpdate(BaseModel):

    name: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=100
    )

    email: Optional[EmailStr] = None

    age: Optional[int] = Field(
        default=None,
        ge=18,
        le=100
    )


class UserResponse(BaseModel):

    id: int

    name: str

    email: EmailStr

    age: int

    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )

    @computed_field
    @property
    def is_adult(self) -> bool:

        return self.age >= 18


class UserLogin(BaseModel):

    email: EmailStr

    password: str


class UserFilter(BaseModel):

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

    min_age: Optional[int] = None

    max_age: Optional[int] = None