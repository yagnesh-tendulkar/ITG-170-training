from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name:  str        # must be text
    email: EmailStr   # must be valid email like abc@gmail.com
class UserUpdate(BaseModel):
    name: Optional[str] =None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] =None
class UserResponse(BaseModel):
    id : int
    name:str
    is_active: bool
    created_at: Optional[datetime]

    class Config:
        from_attributes = True