# app/models/book_db.py
from app.schemas.book_schema import Book

# Acts as our persistent data layer for learning
db_inventory: dict[int, Book] = {
    1: Book(id=1, title="Clean Code", author="Robert C. Martin", price=42.50, in_stock=True),
    2: Book(id=2, title="You Don't Know JS", author="Kyle Simpson", price=25.00, in_stock=False)
}