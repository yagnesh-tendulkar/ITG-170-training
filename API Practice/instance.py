from fastapi import FastAPI

# Define everything directly inside the instance creation block
pb = FastAPI(
    title="Production Grade API",
    version="2.1.0",
    docs_url="/interactive-playground" # This works perfectly with uvicorn reloads!
)
DB={}
@pb.get("/")
def read_root():
    return {"message": "Success"}

@pb.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id < 0:
        return {"error": "Invalid item ID"}
    elif item_id > 100:
        return {"error": "Item ID too large"}
    elif item_id in DB:
        return {"item_id": item_id, "name": DB[item_id]}
    else:
        return {"item_id": item_id, "message": f"Item {item_id} not found"}


@pb.post("/create/{name}")
def create_item(name: str):
    item_id = len(DB) + 1
    DB[item_id] = name
    return {"item_id": item_id, "name": name, "message": "Item created successfully"}
