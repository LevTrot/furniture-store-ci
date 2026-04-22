from sqlalchemy.orm import Session
from app.models.product import Product


def create(db: Session, data):
    product = Product(**data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_all(db: Session):
    return db.query(Product).all()


def get(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def update(db: Session, product_id: int, data):
    product = get(db, product_id)
    if not product:
        return None
    for key, value in data.dict().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product


def delete(db: Session, product_id: int):
    product = get(db, product_id)
    if not product:
        return None
    db.delete(product)
    db.commit()
    return product