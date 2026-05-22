from fastapi import FastAPI
from pydantic import BaseModel

# class User(BaseModel):
#     name:str
#     age:int
app=FastAPI()
# @app.get("/users/{name}")
# def get_user(name):
#     return {"name":name}
# @app.get("/items")
# def get_details(name:str=None,price:int=0):
#     return {
#         "name":name,
#         "price":price
#     }
# @app.post("/user_data")
# def user_data(user:User):
#     return {
#         "user_data":user
#     }

class Address(BaseModel):
    city:str
    pin:str

class User(BaseModel):
    name:str
    age:int
    email:str
    address:Address


@app.post("/get_user")
def user_data(user:User):
    return {
        "data":user
    }
