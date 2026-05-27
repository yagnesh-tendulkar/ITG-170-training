from sqlalchemy.orm import Session
from models import Book


def create_book(db: Session, book_data):
    new_book = Book(**book_data.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def get_all_books(db: Session):
    return db.query(Book).all()


def get_single_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def update_book(db: Session, book_id: int, updated_data):
    book = get_single_book(db, book_id)

    if book:
        for key, value in updated_data.dict().items():
            setattr(book, key, value)

        db.commit()
        db.refresh(book)

    return book


def delete_book(db: Session, book_id: int):
    book = get_single_book(db, book_id)

    if book:
        db.delete(book)
        db.commit()

    return book