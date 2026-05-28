from sqlalchemy.orm import Session
from app.models.product_model import Product

def create_product(
        db:Session,
        product_data
):
    new_product = Product(
        name = product_data.name,
        price=product_data.price,
        quantity=product_data.quantity,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
def get_all_products(db:Session):
    return db.query(Product).all()
def update_product(
        db:Session,
        product_id:int,
        product_data
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return None
    product.name = product_data.name
    product.price = product_data.price
    product.quantity = product_data.quantity

    db.commit()

    db.refresh(product)

    return product
def delete_product(
    db: Session,
    product_id: int
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return None

    db.delete(product)

    db.commit()

    return product