from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query
from sqlalchemy.orm import Session

from database import get_db
from schemas import BookCreate
from schemas import BookUpdate
import crud
from util.status_loader import STATUS_CODES

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/")
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):

    existing_book = db.query(crud.Book).filter(
        crud.Book.title == book.title
    ).first()

    if existing_book:
        raise HTTPException(
            status_code=STATUS_CODES["DUPLICATE_BOOK"]["status_code"],
            detail=STATUS_CODES["DUPLICATE_BOOK"]["message"]
        )

    new_book = crud.create_book(db, book)

    return {
        "status": STATUS_CODES["BOOK_CREATED"]["status_code"],
        "message": STATUS_CODES["BOOK_CREATED"]["message"],
        "data": new_book
    }


@router.get("/")
def get_books(
    genre: str = Query(None),
    min_price: float = Query(None),
    db: Session = Depends(get_db)
):

    books = crud.get_all_books(db)

    if genre:
        books = [book for book in books if book.genre == genre]

    if min_price:
        books = [book for book in books if book.price >= min_price]

    return books


@router.get("/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):

    book = crud.get_single_book(db, book_id)

    if not book:
        raise HTTPException(
            status_code=STATUS_CODES["BOOK_NOT_FOUND"]["status_code"],
            detail=STATUS_CODES["BOOK_NOT_FOUND"]["message"]
        )

    return book


@router.put("/{book_id}")
def update_existing_book(
    book_id: int,
    updated_book: BookUpdate,
    db: Session = Depends(get_db)
):

    book = crud.update_book(db, book_id, updated_book)

    if not book:
        raise HTTPException(
            status_code=STATUS_CODES["BOOK_NOT_FOUND"]["status_code"],
            detail=STATUS_CODES["BOOK_NOT_FOUND"]["message"]
        )

    return {
        "status": STATUS_CODES["BOOK_UPDATED"]["status_code"],
        "message": STATUS_CODES["BOOK_UPDATED"]["message"],
        "data": book
    }


@router.delete("/{book_id}")
def remove_book(book_id: int, db: Session = Depends(get_db)):

    deleted_book = crud.delete_book(db, book_id)

    if not deleted_book:
        raise HTTPException(
            status_code=STATUS_CODES["BOOK_NOT_FOUND"]["status_code"],
            detail=STATUS_CODES["BOOK_NOT_FOUND"]["message"]
        )

    return {
        "status": STATUS_CODES["BOOK_DELETED"]["status_code"],
        "message": STATUS_CODES["BOOK_DELETED"]["message"]
    }