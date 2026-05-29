# Restaurant Backend Responsibilities

# A restaurant app backend handles:

# customers
# menu items
# orders
# table bookings
# payments
# delivery status

from fastapi import FastAPI 
from pydantic import BaseModel,Field

app  = FastAPI()
DATABASE = {
    "customers": {
        "101": {
            "name": "kalyan",
            "phone": "98765455",
            "address": "CPT"
        },
        "102": {
            "name": "balaji",
            "phone": "987654551",
            "address": "CPT"
        }
    },
    "menu items": {
        "category": {
            "biryani": {
                "1b": {
                    "name": "chicken biryani",
                    "price": "250"
                },
                "2b": {
                    "name": "chicken dum biryani",
                    "price": "259"
                }
            }, # <-- Closed biryani section cleanly
            "palav": {
                "1b": {
                    "name": "chicken palav",
                    "price": "289"
                },
                "2b": {
                    "name": "natu kodi palav",
                    "price": "279"
                }
            } # <-- Added missing close for palav
        } # <-- Added missing close for category
    }, # <-- Added missing close for menu items
    "orders": {
        "delivery": {
            "order_id": {
                "1": {
                    "status": "delivered"
                }
            }
        }
    },
    "table bookings": {
        "tableno": {
            "A": {
                "status": "Booked"
            },
            "B": {
                "status": "Unbooked"
            }
        }
    }
} # <-- Closes the main DATABASE dictionary perfectly



class Menu(BaseModel):
    category:str
    item_id:str
    item_name:str
    item_price:int

class Customer(BaseModel):
    name:str
    phone:int
    address:str

class MenuUpdate(BaseModel):
    item_name: str
    item_price: int



@app.get("/")
def get_menu():
    return "!!! welcome to PSR cuisine!!!"

@app.get("/customer")
def get_customer():
    return DATABASE["customers"]

@app.get("/orders")
def get_orders():
    return DATABASE["orders"]

@app.get("/tablebook")
def get_booking():
    return DATABASE["table bookings"]


@app.get("/menu items")
def get_menu():
    return DATABASE["menu items"]

@app.post("/menu items")
def create_menu(item: Menu):
    # 1. Reach the core 'category' dictionary inside your DATABASE
    menu_categories = DATABASE["menu items"]["category"]
    
    # 2. Check if the user's category (e.g., "biryani") exists. 
    #    If it doesn't exist yet, create a blank dictionary for it!
    if item.category not in menu_categories:
        menu_categories[item.category] = {}
        
    # 3. Check if this item ID already exists to avoid overwriting existing dishes
    if item.item_id in menu_categories[item.category]:
        return {"error": f"Item ID {item.item_id} already exists in {item.category}!"}
        
    # 4. Insert the new item data into the nested structure
    menu_categories[item.category][item.item_id] = {
        "name": item.item_name,
        "price": item.item_price
    }
    
    # 5. Return a success message alongside the updated menu data
    return {
        "message": "Item added successfully!", 
        "current_menu": DATABASE["menu items"]
    }




@app.delete("/menu-items/{category_name}/{item_id}")
def delete_item_by_path(category_name: str, item_id: str):
    # 1. Access the categories folder
    categories = DATABASE["menu items"]["category"]
    
    # 2. Safety check: does the category exist?
    if category_name not in categories:
        return {"error": f"Category '{category_name}' does not exist"}
        
    # 3. Safety check: does the item exist inside that category?
    if item_id not in categories[category_name]:
        return {"error": f"Item ID '{item_id}' not found in '{category_name}'"}
        
    # 4. Perform the deletion
    del categories[category_name][item_id]
    
    return {
        "status": "Success",
        "message": f"Deleted item {item_id} from {category_name}"
    }


# We reuse your existing Menu schema to validate the incoming update data
@app.put("/menu-items/{category_name}/{item_id}/")
def update_menu_item(category_name: str, item_id: str, updated_item: MenuUpdate):
    # 1. Access the categories folder
    categories = DATABASE["menu items"]["category"]
    
    # 2. Check if the category exists
    if category_name not in categories:
        return {"error": f"Category '{category_name}' does not exist"}
        
    # 3. Check if the item actually exists before trying to update it
    if item_id not in categories[category_name]:
        return {"error": f"Item ID '{item_id}' not found inside '{category_name}'. Cannot update."}
        
    # 4. Overwrite the old values with the new data from the Request Body
    categories[category_name][item_id] = {
        "name": updated_item.item_name,
        "price": str(updated_item.item_price) # Ensuring it stays as a string in your DB
    }
    
    return {
        "status": "Success",
        "message": f"Item {item_id} inside {category_name} has been updated!",
        "updated_item": categories[category_name][item_id]
    }