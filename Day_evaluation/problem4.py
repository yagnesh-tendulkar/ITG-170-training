from fastapi import FastAPI
from pydantic import BaseModel,field_validator

app=FastAPI()

class geetha(BaseModel):

    name:str
    age:int
    @field_validator('age')
    def validate_age(cls,value):
        if value < 18:
            raise ValueError(" age must be greter than 18")
        return value
@app.post("/user")
async def create_geetha(user:geetha):

    return {
        "message":"user created successfully",
        "dta":user
    }
