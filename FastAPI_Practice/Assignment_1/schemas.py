from pydantic import BaseModel, Field

class Book(BaseModel):
    book_id: int = Field(gt=-1)
    book_title: str = "Book_"+ str(book_id)
    book_description: str 
    