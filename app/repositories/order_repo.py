from sqlalchemy.orm import Session
from app.models.order import Order


def create(db: Session):
    order = Order()
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def get_all(db: Session):
    return db.query(Order).all()


def get(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def delete(db: Session, order_id: int):
    order = get(db, order_id)
    if not order:
        return None
    db.delete(order)
    db.commit()
    return order