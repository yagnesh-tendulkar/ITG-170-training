from pydantic import BaseModel, Field
from typing import Optional

class Book(BaseModel):
    id: int = Field(..., description="Unique identifier for the book")
    title: str = Field(..., min_length=1, max_length=100, example="The Pragmatic Programmer")
    author: str = Field(..., min_length=1, max_length=50, example="Andy Hunt")
    price: float = Field(..., gt=0, example=39.99)
    in_stock: bool = Field(default=True)

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    author: Optional[str] = Field(None, min_length=1, max_length=50)
    price: Optional[float] = Field(None, gt=0)
    in_stock: Optional[bool] = None