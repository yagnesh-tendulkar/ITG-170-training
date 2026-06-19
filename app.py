from fastapi import FastAPI
from models import Menu

# FastAPI application create chestunnam
app = FastAPI()

# temporary database
menu = []


# Home API
@app.get("/")
def home():

    return {
        "message": "welcome to geetha's kitchen"
    }


# GET all dishes
@app.get("/menu")
def get_menu():

    return menu


# CREATE dish
@app.post("/menu")
def create_a_dish(dish: Menu):

    # new dish add chestunnam
    menu.append(dish.model_dump())

    return {
        "message": "dish added successfully",
        "added": dish
    }


# UPDATE dish
@app.put("/menu/{dish_id}")
def update_the_dish(dish_id: int, dish1: Menu):

    for i in menu:

        # current item id check
        if i["id"] == dish_id:

            # values update chestunnam
            i["name"] = dish1.name
            i["price"] = dish1.price
            i["quantity"] = dish1.quantity

            return {
                "message": "successfully updated",
                "data": i
            }

    return {
        "error": "dish not found"
    }


# DELETE dish
@app.delete("/menu/{dish_id}")
def remove_dish(dish_id: int):

    for i in menu:

        # id compare chestunnam
        if i["id"] == dish_id:

            # item remove chestunnam
            menu.remove(i)

            return {
                "message": "dish deleted"
            }

    return {
        "error": "dish not found"
    }