from datetime import datetime

from pydantic import BaseModel
from ecommerce.products.schema import ProductListing


class ShowOrderDetails(BaseModel):
    id: int
    order_id: int
    product_order_details: ProductListing

    class Config:
        orm_mode = True


class ShowOrder(BaseModel):
    id: int | None
    order_date: datetime
    order_amount: float
    order_status: str
    shipping_address: str
    order_details: list[ShowOrderDetails] = []

    class Config:
        orm_mode = True
