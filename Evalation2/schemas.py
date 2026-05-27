from pydantic import BaseModel, Field, field_validator
from validators.product_validator import validate_product_name


class ProductBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    category: str = Field(..., min_length=2, max_length=100)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    brand: str = Field(..., min_length=2, max_length=100)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        return validate_product_name(value)

    @field_validator("brand")
    @classmethod
    def validate_brand(cls, value):
        if value.lower() == "unknown":
            raise ValueError("Brand cannot be unknown")
        return value


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True