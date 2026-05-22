from fastapi import FastAPI,Header
from pydantic import BaseModel
app=FastAPI()
@app.get("/users")
def get_users(user_id:int=Header(None),
              name:str=Header(None)):
    return {
        "user_id":user_id,
        "name":name
    }

