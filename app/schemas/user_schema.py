from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
    computed_field,
    EmailStr
)
from typing import Optional


class CreateUser(BaseModel):
    first_name : str
    last_name : str
    email : EmailStr
    age : int
    password : str
    confirm_password : str

    @field_validator("password")
    def validate_password(cls,value):
        if len(value) < 8:
            raise ValueError(
                "Password must contains at least 8 character"
            )
        return value
    
    @model_validator(mode="after")
    def confirm_pass(self):
        if self.password != self.confirm_password:
            raise ValueError(
                "Confirm Password should match with password"
            )   
        return self


class UserLogin(BaseModel):
    email : EmailStr
    password : str

class UpdateUser(BaseModel):
    email : Optional[EmailStr] = None
    password : Optional[str] = None
    age : Optional[int] = None

class UserResponse(BaseModel):

    id: int
    email: EmailStr
    first_name:str
    last_name:str
    age: int
    @computed_field
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
   