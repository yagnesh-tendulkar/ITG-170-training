from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Home Route
@app.get("/")
def home():
    return {"message": "Hello World"}


#         password="M1racle@123",   # keep correct one
# Product Model
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int


# Sample Products List
products = [
    Product(
        id=1,
        name="Phone",
        description="Budget Phone",
        price=99,
        quantity=10
    ),
    Product(
        id=2,
        name="MacBook",
        description="Budget Laptop",
        price=999,
        quantity=6
    )
]


# Get All Products
@app.get("/products")
def get_all_products():
    return products


# Student Model
class Student(BaseModel):
    name: str
    age: int


# Create Student API
@app.post("/students")
def create_student(student: Student):
    return student