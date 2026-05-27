from sqlalchemy.orm import Session
from models import Product

def create_product(db: Session, product):
    new_product = Product(
        name=product.name,
        category=product.category,
        price=product.price,
        stock=product.stock,
        brand=product.brand
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


# GET ALL PRODUCTS

def get_all_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()


# GET SINGLE PRODUCT

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


# UPDATE PRODUCT

def update_product(db: Session, product_id: int, product_data):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        return None

    product.name = product_data.name
    product.category = product_data.category
    product.price = product_data.price
    product.stock = product_data.stock
    product.brand = product_data.brand

    db.commit()
    db.refresh(product)

    return product


# DELETE PRODUCT

def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        return None

    db.delete(product)
    db.commit()

    return product