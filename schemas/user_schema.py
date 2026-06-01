from pydantic import (
    BaseModel,
    EmailStr,
    field_validator,
    model_validator,
)

from typing import Optional


class CreateUser(BaseModel):

    first_name: str
    last_name: str
    email: EmailStr
    age: int
    password: str
    confirm_password: str

    @field_validator("age")
    def validate_age(cls, value):

        if value < 18:
            raise ValueError(
                "Age must be greater than or equal to 18"
            )

        return value

    @field_validator("password")
    def validate_password(cls, value):

        if len(value) < 8:
            raise ValueError(
                "Password must contain at least 8 characters"
            )

        return value

    @model_validator(mode="after")
    def validate_confirm_password(self):

        if self.password != self.confirm_password:
            raise ValueError(
                "Passwords do not match"
            )

        return self


class UserLogin(BaseModel):

    email: EmailStr
    password: str


class UpdateUser(BaseModel):

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[EmailStr] = None
