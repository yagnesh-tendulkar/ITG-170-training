from fastapi import APIRouter, HTTPException, status
from typing import List
# Import the schemas we just moved above
from app.schemas.book_schema import Book, BookUpdate

router = APIRouter()

# In-Memory Database moved here for now
db_inventory = {
    1: Book(id=1, title="Clean Code", author="Robert C. Martin", price=42.50, in_stock=True),
    2: Book(id=2, title="You Don't Know JS", author="Kyle Simpson", price=25.00, in_stock=False)
}


@router.get("/")
async def root():
    return {"message": "Welcome to the Book Inventory API!"}

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book: Book):
    if book.id in db_inventory:
        raise HTTPException(status_code=400, detail="Book already exists.")
    db_inventory[book.id] = book
    return book

@router.get("/all", response_model=List[Book])
async def get_all_books():
    return list(db_inventory.values())

@router.get("/{book_id}", response_model=Book)
async def get_book_by_id(book_id: int):
    if book_id not in db_inventory:
        raise HTTPException(status_code=404, detail="Book not found.")
    return db_inventory[book_id]

@router.put("/{book_id}", response_model=Book)
async def update_book(book_id: int, book_update: BookUpdate):
    if book_id not in db_inventory:
        raise HTTPException(status_code=404, detail="Book not found.")
    current_book = db_inventory[book_id]
    update_data = book_update.model_dump(exclude_unset=True)
    updated_book = current_book.model_copy(update=update_data)
    db_inventory[book_id] = updated_book
    return updated_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    if book_id not in db_inventory:
        raise HTTPException(status_code=404, detail="Book not found.")
    del db_inventory[book_id]
    return None