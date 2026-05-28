from fastapi import FastAPI, Query, Path, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

books = []
class Book(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=50)
    author: str
    price: float = Field(gt=0)

@app.get("/")
def home():
    return {
        "message": "Welcome to Book API"
    }

@app.post("/books", status_code=status.HTTP_201_CREATED)
def add_book(book: Book):
    books.append(book)
    return {
        "message": "Book Added Successfully",
        "data": book
    }

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book_by_id(
    book_id: int = Path(
        ...,
        gt=0,
        description="Enter Book ID"
    )
):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book Not Found"
    )

@app.get("/search")
def search_book(
    name: str = Query(
        ...,
        min_length=2,
        description="Search Book Name"
    )
):
    result = []
    for book in books:
        if name.lower() in book.name.lower():
            result.append(book)
    return result

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index in range(len(books)):
        if books[index].id == book_id:
            books[index] = updated_book
            return {
                "message": "Book Updated Successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book Not Found"
    )

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index in range(len(books)):
        if books[index].id == book_id:
            books.pop(index)
            return {
                "message": "Book Deleted Successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book Not Found"
    )