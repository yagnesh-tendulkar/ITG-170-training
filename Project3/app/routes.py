from typing import List

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas import (
    ProductCreate,
    ProductResponse
)

from app.services import (
    create_product,
    get_products,
    update_product,
    delete_product
)

from app.exceptions import (
    ProductNotFoundException
)

from app.constants_loader import (
    STATUS_CODES,
    ERROR_MESSAGES
)


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


# CREATE PRODUCT
@router.post(
    "/",
    response_model=ProductResponse,
    status_code=STATUS_CODES[
        "HTTP_201_CREATED"
    ]
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
    status_code=STATUS_CODES[
        "HTTP_200_OK"
    ]
)
def fetch_products(
    db: Session = Depends(get_db)
):

    return get_products(db)


# UPDATE PRODUCT
@router.put(
    "/{product_id}",
    response_model=ProductResponse,
    status_code=STATUS_CODES[
        "HTTP_200_OK"
    ]
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

        raise ProductNotFoundException()

    return updated_product


# DELETE PRODUCT
@router.delete(
    "/{product_id}",
    status_code=STATUS_CODES[
        "HTTP_200_OK"
    ]
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

        raise ProductNotFoundException()

    return {
        "message": ERROR_MESSAGES[
            "PRODUCT_DELETED"
        ]
    }