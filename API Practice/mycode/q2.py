#create a FastAPI application with CRUD operations for a simple in-memory product inventory. Each product should have an ID, category, and quantity. Implement the following endpoints:
#1. GET /products - Retrieve a list of all products.
#2. POST /products - Create a new product (ID passed in URL, body details passed via Pydantic).
#3. PUT /products/{id} - Update an existing product (ID passed in URL, body details passed via Pydantic).
#4. DELETE /products/{id} - Delete a product by ID. 
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

opr = FastAPI()

# In-memory database
Products = [{"id": 1, "categ": "Laptop", "quant": 1000}]

# Pydantic Schemas
class ProductCreate(BaseModel):
    id: int
    categ: str
    quant: int

class ProductUpdate(BaseModel):
    categ: str
    quant: int    

# --- CRUD Operations ---

# 1. READ ALL (200 OK is default)
@opr.get("/products")
def get_products():
    return {"products": Products}

# 2. CREATE (Explicitly returns 201 Created)
@opr.post("/products", status_code=status.HTTP_201_CREATED)
def create_prod(prod: ProductCreate):
    # Check if product already exists
    if any(p["id"] == prod.id for p in Products):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Product with this ID already exists"
        )
    
    new_prod = prod.model_dump() # Converts Pydantic model to dict
    Products.append(new_prod)
    return {"message": "Product created successfully", "product": new_prod}

# 3. UPDATE (200 OK is default)
@opr.put("/products/{id}")
def update_prod(id: int, prod: ProductUpdate):
    for p in Products:
        if p["id"] == id:
            p["categ"] = prod.categ
            p["quant"] = prod.quant
            return {"message": "Product updated successfully", "product": p}
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Product not found"
    )

# 4. DELETE (204 No Content is standard, or 200 OK with a message)
@opr.delete("/products/{id}", status_code=status.HTTP_200_OK)
def delete_prod(id: int):
    for p in Products:
        if p["id"] == id:
            Products.remove(p)
            return {"message": f"Product with ID {id} deleted successfully"}
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Product not found"
    )