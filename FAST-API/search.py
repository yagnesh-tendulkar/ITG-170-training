from fastapi import FastAPI
from typing import Optional
app=FastAPI()
products=[
    { "id":1,"name":"pen","category":"stationary","price": 30},
{ "id":2,"name":"pencil","category":"stationary","price": 20},
{ "id":3,"name":"T-shirt","category":"clothing","price": 1000},
{ "id":4,"name":"eraser","category":"stationary","price": 30},
]
@app.get("/product")
def get_p(category : Optional[str] =None,price : Optional[int] =None):
    fp=products
    if category :
        fp=[p for p in fp if p["category"].lower()==category.lower()]
    if price:
        fp=[p for p in fp if p['price'] <= price]
    return fp