from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class User(BaseModel):
    username: str
@app.post("/user")
async def create_user(user: User):
    return {"username": user.username}
@app.get("/user")
async def get_user(username: str):
    return {"username": username}
