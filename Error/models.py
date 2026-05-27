from pydantic import BaseModel, Field

class UserRequest(BaseModel):
    name: str = Field(..., min_length=3)
    age: int = Field(..., gt=0)
    email: str