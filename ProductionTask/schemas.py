from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name:str=Field(...,min_length=2)
    age:int=Field(...,ge=5,le=100)
    email:EmailStr
    course:str
class UpdateStudent(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    email:Optional[EmailStr]=None
    course:Optional[str]=None