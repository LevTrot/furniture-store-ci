from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas.product import ProductCreate, ProductOut, ProductUpdate 
from app.repositories import product_repo

router = APIRouter(prefix="/products", tags=["products"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ProductOut)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    return product_repo.create(db, data)


@router.get("/", response_model=list[ProductOut])
def get_products(db: Session = Depends(get_db)):
    return product_repo.get_all(db)


@router.put("/{product_id}", response_model=ProductOut)
def update_product(product_id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    return product_repo.update(db, product_id, data)


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return product_repo.delete(db, product_id)