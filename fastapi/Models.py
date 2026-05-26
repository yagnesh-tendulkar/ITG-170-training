from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()
@app.post("/age/{p_age}")
async def add_age(p_age:int):
    return {"age_received": p_age, "message": "Age added successfully"}
@app.post("/age/{p_age}")
async def add_age(p_age:int):
    return {"age_received": p_age, "message": "Age added successfully"}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

