from sqlalchemy import Column, Integer, String, ForeignKey
from app.db import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))