from datetime import datetime

from pydantic import BaseModel

from ecommerce.products.schema import Product


class ShowCartItems(BaseModel):
    id: int
    products: Product
    cart_data: datetime

    class Config:
        orm_mode = True


class ShowCart(BaseModel):
    id: int
    cart_items: list[ShowCartItems] = []

    class Config:
        orm_mode = True
