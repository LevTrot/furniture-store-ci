from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas.category import CategoryCreate, CategoryOut, CategoryUpdate 
from app.repositories import category_repo

router = APIRouter(prefix="/categories", tags=["categories"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=CategoryOut)
def create_category(data: CategoryCreate, db: Session = Depends(get_db)):
    return category_repo.create(db, data.name)


@router.get("/", response_model=list[CategoryOut])
def get_categories(db: Session = Depends(get_db)):
    return category_repo.get_all(db)


@router.put("/{category_id}", response_model=CategoryOut)
def update_category(category_id: int, data: CategoryUpdate, db: Session = Depends(get_db)):
    return category_repo.update(db, category_id, data.name)


@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return category_repo.delete(db, category_id)