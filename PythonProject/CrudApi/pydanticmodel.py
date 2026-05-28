from typing import Optional

from pydantic import BaseModel,EmailStr,field_validator
class User(BaseModel):
    name:str
    age:int
    email:EmailStr
    @field_validator("age")
    @classmethod
    def check_age(cls,age):
        if age<0:
            raise ValueError("age cannot be -ve")
        return age
dict={"name":"rudra","age":23,"email":"sibun@gmail.com"}
user =User(**dict)
print(user)

class UpdateUser(BaseModel):
    name: str
    age: int

    @field_validator("age")
    @classmethod
    def check_age(cls, age):
        if age < 0:
            raise ValueError("age cannot be -ve")
        return age
class PatchUser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None