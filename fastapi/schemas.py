from pydantic import BaseModel

# CREATE
class UserCreate(BaseModel):
    first_name: str
    last_name: str


# RESPONSE
class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        from_attributes = True