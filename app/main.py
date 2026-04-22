from fastapi import FastAPI
from app.db import Base, engine
from app.routers import category_router, product_router, order_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(category_router.router)
app.include_router(product_router.router)
app.include_router(order_router.router)