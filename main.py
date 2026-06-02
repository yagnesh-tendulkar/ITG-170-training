
from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int


# GET Method
@app.get("/students/{id}")
def getting_user(id: int,user_name:str=None,user_number:int=None):
    return {
        "student_id": id,
        "student_name": user_name,
        "student_number": user_number
    }


# POST Method
@app.post("/posts/{id}")
def posting(id: int, user_name: str, user_number: int):
    return {
        "student_id": id,
        "student_name": user_name,
        "student_number": user_number
    }


# Main Function
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)