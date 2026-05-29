from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name:str
    f_name:str
    l_name:str

@app.get("/")
#get method that greets an user when he typed url 
def greet():
    return {'message':'welcome to balaji services'}


@app.get("/user/{name}")
def user(name:str):
    return {"message":f"{name}"}

@app.post("/user")
def user_details(user:User) :
    return {"message ": user}   

# @app.get("/user/{f_name}")
# def get_details(f_name:str):
#     return {"message"}

@app.put("/user/{l_name}")
def update_details(name:str,f_name:str,l_name:str):
    return {"message ": f"User details are updated :Name:{name},First Name:{f_name},Last Name:{l_name}"}


@app.delete("/user/{name}")
def delete_user(user:User):
    return {"message":f"user deleted"}
