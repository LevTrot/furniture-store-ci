from sqlalchemy.orm import Session
from app.models.category import Category


def create(db: Session, name: str):
    category = Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_all(db: Session):
    return db.query(Category).all()


def get(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def update(db: Session, category_id: int, name: str):
    category = get(db, category_id)
    if not category:
        return None
    category.name = name
    db.commit()
    db.refresh(category)
    return category


def delete(db: Session, category_id: int):
    category = get(db, category_id)
    if not category:
        return None
    db.delete(category)
    db.commit()
    return category