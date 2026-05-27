from pydantic import BaseModel, field_validator
from fastapi import FastAPI
app = FastAPI()

class User(BaseModel):

    age:int
    @field_validator("age")
    def check_age(cls, v):
        if v < 18:
            raise ValueError ("Age must be gretaer than 18")
        return v
@app.post("/age")
def read_age(user:User):
    return {
        "User": user,
        "Age": user.age
    }