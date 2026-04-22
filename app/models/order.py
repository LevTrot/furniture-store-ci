from sqlalchemy import Column, Integer, Table, ForeignKey
from app.db import Base

order_products = Table(
    "order_products",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id")),
    Column("product_id", ForeignKey("products.id"))
)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)