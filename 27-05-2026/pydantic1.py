from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
#creating pydantic model
class User(BaseModel):
    name : str
    age : int

@app.get('/user')
def get_user(user:User):
    return user
    