from pydantic import BaseModel, field_validator


class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    price: float

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if len(value.strip()) < 3:
            raise ValueError("Title must contain at least 3 characters")
        return value.title()

    @field_validator("price")
    @classmethod
    def validate_price(cls, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero")
        return value


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True