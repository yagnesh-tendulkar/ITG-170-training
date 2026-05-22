from fastapi import FastAPI
app=FastAPI()
@app.get("/user/{user_id}")
def get_user(user_id:int):
    return {"data":user_id}

@app.get("/product")
def get_product(product_id:int,product_name:str):
    return {
        "name":product_name,
        "id":product_id
    }