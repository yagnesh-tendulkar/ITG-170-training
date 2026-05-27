from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
app = FastAPI()
class Person(BaseModel):
    name: str
    email: str
    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        if "@gmail.com" not in value:
            raise ValueError("Only Gmail emails are allowed")
        return value
@app.post("/person")
def details(p: Person):
    return {"email": p.email, "name": p.name}
