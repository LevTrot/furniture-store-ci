from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.repositories import order_repo

router = APIRouter(prefix="/orders", tags=["orders"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_order(db: Session = Depends(get_db)):
    return order_repo.create(db)


@router.get("/")
def get_orders(db: Session = Depends(get_db)):
    return order_repo.get_all(db)


@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return order_repo.delete(db, order_id)