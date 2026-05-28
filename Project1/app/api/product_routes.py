from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.product_schema import (
    ProductCreate,
    ProductResponse
)

from app.services.product_services import (
    create_product,
    get_all_products,
    update_product,
    delete_product
)


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


# CREATE PRODUCT
@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    return create_product(
        db,
        product
    )


# GET ALL PRODUCTS
@router.get(
    "/",
    response_model=List[ProductResponse],
    status_code=status.HTTP_200_OK
)
def fetch_products(
    db: Session = Depends(get_db)
):

    return get_all_products(db)


# UPDATE PRODUCT
@router.put(
    "/{product_id}",
    response_model=ProductResponse,
    status_code=status.HTTP_200_OK
)
def modify_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    updated_product = update_product(
        db,
        product_id,
        product
    )

    if not updated_product:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return updated_product


# DELETE PRODUCT
@router.delete(
    "/{product_id}",
    status_code=status.HTTP_200_OK
)
def remove_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    deleted_product = delete_product(
        db,
        product_id
    )

    if not deleted_product:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return {
        "message": "Product deleted successfully"
    }