from fastapi import APIRouter, Query

from schemas.book_schema import BookCreate

from services.book_service import (
    create_book,
    get_all_books,
    get_single_book,
    update_book,
    delete_book
)

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


# CREATE BOOK
@router.post("/")
async def add_book(data: BookCreate):

    return create_book(data)


# GET ALL BOOKS USING QUERY PARAMETERS
@router.get("/")
async def fetch_books(
    author: str = Query(None),
    price: int = Query(None)
):

    return get_all_books(author, price)


# GET SINGLE BOOK USING PATH PARAMETER
@router.get("/{book_id}")
async def fetch_single_book(book_id: int):

    return get_single_book(book_id)


# UPDATE BOOK
@router.put("/{book_id}")
async def edit_book(
    book_id: int,
    data: BookCreate
):

    return update_book(book_id, data)


# DELETE BOOK
@router.delete("/{book_id}")
async def remove_book(book_id: int):

    return delete_book(book_id)