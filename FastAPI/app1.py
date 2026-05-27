from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Student(BaseModel):
    name: str
    salary: int

@app.get("/")
def home():
    return {"Hello": "World"}
@app.get("/student")
def get_student():
    return {
        "name": "Arika",
        "salary": 50000
    }
