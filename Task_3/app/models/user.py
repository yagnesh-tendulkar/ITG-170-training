from pydantic import BaseModel
from fastapi import FastAPI
app=FastAPI()
class User(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:str
