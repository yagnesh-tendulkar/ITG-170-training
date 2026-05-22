# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def home():
#     return {"message": "Hello FastAPI"}
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def program():
#     return {"message": "Hello FastAPI"}
# from fastapi import FastAPI
# app =FastAPI()
# @app.get("/")
# def sending_data():
#     return {"message": "I have the Secret code"}
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/users/{id}")
# def read_data_from_user(id: int):
#     return {"user_id": id}
# pip install sqlalchemy
from fastapi import FastAPI
from database import engine
from models import Base

app = FastAPI()   # MUST be present

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "working"}
from pydantic import BaseModel
from database import SessionLocal
from models import Item

class ItemSchema(BaseModel):
    name: str
    price: int

@app.post("/items/")
def create_item(item: ItemSchema):
    db = SessionLocal()
    db_item = Item(name=item.name, price=item.price)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item
