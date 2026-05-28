from sqlmodel import SQLModel, Field
from pydantic import field_validator, model_validator, computed_field
from typing import Optional


class DeveloperProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    experience_years: int
    password: str
    confirm_password: str

    @field_validator("experience_years")
    @classmethod
    def check_realistic_experience(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Experience years cannot be negative.")
        if value > 90:
            raise ValueError("That is an impressive career, but please double-check your experience years.")
        return value

    @model_validator(mode="after")
    def verify_password_match(self) -> "DeveloperProfile":
        if self.password != self.confirm_password:
            raise ValueError("The password and password confirmation do not match.")
        return self

    @computed_field
    @property
    def developer_tier(self) -> str:
        if self.experience_years == 0:
            return "Intern / Fresher"
        elif self.experience_years < 3:
            return "Junior Developer"
        elif self.experience_years < 6:
            return "Mid-Level Developer"
        else:
            return "Senior Architect"
