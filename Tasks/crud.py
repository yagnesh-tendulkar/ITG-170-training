from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str


# CREATE
@app.post("/items/")
async def create_item(item: Item):
    return item


# READ
@app.get("/items")
async def get_items():
    return [{"name": "Laptop"}, {"name": "Mobile"}]


# UPDATE
@app.put("/items/{item_name}")
async def update_item(item_name: str, item: Item):
    return {
        "updated_item": item_name,
        "new_data": item
    }


# DELETE
@app.delete("/items/{item_name}")
async def delete_item(item_name: str):
    return {"deleted_item": item_name}
