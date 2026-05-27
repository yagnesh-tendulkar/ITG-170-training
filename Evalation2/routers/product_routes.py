from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session

from database import get_db
from schemas import ProductCreate, ProductUpdate, ProductResponse
import crud
from constants import status_codes

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# GET ALL PRODUCTS WITH QUERY PARAMETERS
@router.get(
    "/",
    response_model=list[ProductResponse],
    status_code=status_codes.SUCCESS
)
def fetch_products(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return crud.get_all_products(db, skip, limit)

@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status_codes.CREATED
)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)


# GET PRODUCT USING PATH PARAMETER
@router.get(
    "/{product_id}",
    response_model=ProductResponse,
    status_code=status_codes.SUCCESS
)
def fetch_single_product(
    product_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    product = crud.get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(
            status_code=status_codes.NOT_FOUND,
            detail="Product not found"
        )

    return product


# UPDATE PRODUCT
@router.put(
    "/{product_id}",
    response_model=ProductResponse,
    status_code=status_codes.UPDATED
)
def modify_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db)
):
    updated_product = crud.update_product(db, product_id, product)

    if not updated_product:
        raise HTTPException(
            status_code=status_codes.NOT_FOUND,
            detail="Product not found"
        )

    return updated_product


# DELETE PRODUCT
@router.delete(
    "/{product_id}",
    status_code=status_codes.DELETED
)
def remove_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    deleted_product = crud.delete_product(db, product_id)

    if not deleted_product:
        raise HTTPException(
            status_code=status_codes.NOT_FOUND,
            detail="Product not found"
        )

    return {
        "message": "Product deleted successfully"
    }