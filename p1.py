from fastapi import FastAPI,Request
from pydantic import BaseModel
import time
app=FastAPI()
@app.middleware("http")
async def log_requests(request: Request, call_next):

    print("Request Started")
    print("Method:", request.method)
    print("URL:", request.url)

    start = time.time()

    response = await call_next(request)

    end = time.time()

    print("Request Completed")
    print("Time Taken:", end - start)

    return response
class Product(BaseModel):
    name:str
    price:float
products={
    1:{"name":"laptop","price":50000},
    2:{"name":"tab","price":30000}
}
@app.get("/products")
def get_products():
  return products

@app.get("/products/{product_id}")
def get_product_id(product_id:int):
   if product_id not in products:
      return{
         "error": "product is not found"
      }
   return products[product_id]

@app.post("/products/{product_id}")
def create_product_id(product_id:int,product:Product):
   if product_id not in products:
      return{
         "error":"product not found"
      }
   products[product_id]={
      "name":product.name,
      "price":product.price
   }
   return{
      "message":"updated sucesfully",
      "updated_product":products[product_id]
   }

@app.put("/products/{product_id}")
def update_product_id(product_id: int, product: Product):

    if product_id not in products:
        return {"error": "Product not found"}

    products[product_id] = {
        "name": product.name,
        "price": product.price
    }

    return {
        "message": "Product updated",
        "updated_product": products[product_id]
    }

@app.patch("/products/{product_id}")
def patch_product_id(product_id: int, price: float):

    if product_id not in products:
        return {"error": "Product not found"}

    products[product_id]["price"] = price

    return {
        "message": "Price updated",
        "product": products[product_id]
    }

@app.delete("/products/{product_id}")
def delete_product_id(product_id: int):

    if product_id not in products:
        return {"error": "Product not found"}

    deleted_product = products.pop(product_id)

    return {
        "message": "Product deleted",
        "deleted_product": deleted_product
    }
   
