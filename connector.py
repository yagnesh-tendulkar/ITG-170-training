
from fastapi import FastAPI

import mysql.connector
app = FastAPI()
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="M1racle@123",
    database="product")
cursor=connection.cursor()

@app.get("/products")
def get_products():
    cursor.execute("select * From pro")
    pro=cursor.fetchall()
    return {"product ":pro}
@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/items/{item_id}")
async def read_item(item_id : int):
    return {"item_id": item_id}
@app.get("/product")
def get_all_products():
    return "products"
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

