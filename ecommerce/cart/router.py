from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ecommerce import db
from ecommerce.user.schema import User
from ecommerce.cart import service
from ecommerce.cart import schema


router = APIRouter(
    tags=["Cart"],
    prefix='/cart'
)


@router.get('/add', status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(product_id: int, database: Session = Depends(db.get_db)):
    result = await service.add_to_cart(product_id, database)
    return result


@router.get('/', response_model=schema.ShowCart)
async def get_all_cart_items(database: Session = Depends(db.get_db)):
    result = await service.get_all_items(database)
    return result


@router.delete('/{cart_item_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def remove_cart_item_by_id(cart_item_id: int, database: Session = Depends(db.get_db)):
    return await service.remove_cart_item(cart_item_id, database)
