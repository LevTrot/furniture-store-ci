from pydantic import BaseModel
from typing import List


class OrderCreate(BaseModel):
    product_ids: List[int]


class OrderOut(BaseModel):
    id: int

    class Config:
        from_attributes = True