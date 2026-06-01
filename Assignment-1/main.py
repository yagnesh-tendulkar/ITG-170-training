from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()


class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)


class Product(ProductCreate):
    id: int


products: List[Product] = []


@app.post("/products", response_model=Product, status_code=201)
def create_product(product: ProductCreate):

    new_id = len(products) + 1

    product_data = Product(
        id=new_id,
        name=product.name,
        price=product.price,
        quantity=product.quantity
    )

    products.append(product_data)

    return product_data


@app.get("/products", response_model=List[Product], status_code=200)
def get_products():

    return products


@app.get("/products/{product_id}", response_model=Product, status_code=200)
def get_product(product_id: int):

    for product in products:

        if product.id == product_id:
            return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )


@app.put("/products/{product_id}", response_model=Product, status_code=200)
def update_product(product_id: int, updated_product: ProductCreate):

    for i in range(len(products)):

        if products[i].id == product_id:

            products[i] = Product(
                id=product_id,
                name=updated_product.name,
                price=updated_product.price,
                quantity=updated_product.quantity
            )

            return products[i]

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )


@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int):

    for product in products:

        if product.id == product_id:

            products.remove(product)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )