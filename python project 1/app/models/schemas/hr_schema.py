from pydantic import BaseModel, EmailStr, Field


class HRCreate(BaseModel):
    hr_name: str = Field(..., min_length=2, max_length=50)
    hr_email: EmailStr
    hr_password: str = Field(..., min_length=6, max_length=100)


class HRResponse(BaseModel):
    hr_id: int
    hr_name: str
    hr_email: EmailStr

    class Config:
        from_attributes = True