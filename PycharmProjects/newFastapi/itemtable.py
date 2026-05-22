from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker,declarative_base  #Object-Relational Mapping
app = FastAPI()
DATABASE_URL = "mysql+pymysql://root:M1racle%40123@localhost:3306/itemdb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
class ItemTable(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
Base.metadata.create_all(bind=engine)
class Item(BaseModel):
    id: int
    name: str
    price: float
class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
@app.get("/items")
def get_items():
    db = SessionLocal()
    items = db.query(ItemTable).all()
    db.close()
    return items
@app.get("/items/{id}")
def get_item(id: int):
    db = SessionLocal()
    item = db.query(ItemTable).filter(
        ItemTable.id == id
    ).first()
    if item:
        db.close()
        return item
    db.close()
    return {
        "message": "Item Not Found"
    }
@app.post("/items")
def add_item(item: Item):
    db = SessionLocal()
    new_item = ItemTable(
        id=item.id,
        name=item.name,
        price=item.price
    )
    db.add(new_item)
    db.commit()
    db.close()
    return {
        "message": "Item Added Successfully"
    }
@app.put("/items/{id}")
def update_item(id: int, item: Item):
    db = SessionLocal()
    existing_item = db.query(ItemTable).filter(
        ItemTable.id == id
    ).first()
    if existing_item:
        existing_item.name = item.name
        existing_item.price = item.price
        db.commit()
        db.close()
        return {
            "message": "Item Updated Successfully"
        }
    db.close()
    return {
        "message": "Item Not Found"
    }
@app.patch("/items/{id}")
def patch_item(id: int, item: Item):
    db = SessionLocal()
    existing_item = db.query(ItemTable).filter(
        ItemTable.id == id
    ).first()
    if existing_item:
        existing_item.name = item.name
    if item.price is not None:
        existing_item.price = item.price
        db.commit()
        db.close()
        return {
            "message": "Item Name Patched Successfully"
        }
    db.close()
    return {
        "message": "Item Not Found"
    }
@app.delete("/items/{id}")
def delete_item(id: int):
    db = SessionLocal()
    item = db.query(ItemTable).filter(
        ItemTable.id == id
    ).first()
    if item:
        db.delete(item)
        db.commit()
        db.close()
        return {
            "message": "Item Deleted Successfully"
        }
    db.close()
    return {
        "message": "Item Not Found"
    }