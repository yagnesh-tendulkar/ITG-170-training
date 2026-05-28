from pydantic import BaseModel
from pydantic import Field

class ProductCreate(BaseModel):
    name : str= Field(min_length = 2, max_length = 100)
    price: int = Field(gt =0)
    quantity:int = Field(ge=0)
class ProductResponse(ProductCreate):
    id:int
    class Config:
        from_attributes = True
