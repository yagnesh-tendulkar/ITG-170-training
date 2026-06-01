from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()


# Request Body Model
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


# GET Method
@router.get("/items")
def get_items():
    return {"message": "All items fetched"}


# GET by ID
@router.get("/items/{item_id}")
def get_single_item(item_id: int):
    return {"item_id": item_id}


# POST Method
@router.post("/items")
def create_item(item: Item):
    return {
        "message": "Item created",
        "data": item
    }


# PUT Method
@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {
        "message": "Item fully updated",
        "item_id": item_id,
        "new_data": item
    }


# PATCH Method
@router.patch("/items/{item_id}")
def patch_item(item_id: int, price: float):
    return {
        "message": "Item partially updated",
        "item_id": item_id,
        "updated_price": price
    }


# DELETE Method
@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {
        "message": "Item deleted",
        "deleted_item_id": item_id
    }
