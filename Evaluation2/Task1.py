#Pydantic Model
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users=[]
class Users(BaseModel):
    id : int
    name : str
    salary: int

#create
@app.post("/users")
def create_user(user: Users):
    users.append(user)
    return {
        "Message":"Added Sucessfully",
    }