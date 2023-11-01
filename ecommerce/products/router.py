from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from ecommerce import db
from ecommerce.products import schema
from ecommerce.products import service
from ecommerce.products import validator

router = APIRouter(
    tags=['Products'],
    prefix='/products'
)


@router.post('/category', status_code=status.HTTP_201_CREATED)
async def create_category(request: schema.Category, database: Session = Depends(db.get_db)):
    new_category = await service.create_new_category(request, database)
    return new_category


@router.get('/category', response_model=list[schema.ListCategory])
async def get_all_categories(database: Session = Depends(db.get_db)):
    return await service.get_all_categories(database)


@router.get('/category/{category_id}', response_model=schema.ListCategory)
async def category_by_id(category_id: int, database: Session = Depends(db.get_db)):
    return await service.get_category_by_id(category_id, database)


@router.delete('/category/{category_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_category_by_id(category_id: int, database: Session = Depends(db.get_db)):
    return await service.delete_category_by_id(category_id, database)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_product(request: schema.Product, database: Session = Depends(db.get_db)):
    category = await validator.verify_category_exist(request.category_id, database)
    if not category:
        raise HTTPException(
            status_code=400,
            detail="You have provided invalid category id"
        )
    product = await service.create_new_product(request, database)
    return product


@router.get('/', response_model=list[schema.ProductListing])
async def get_all_product(database: Session = Depends(db.get_db)):
    return await service.get_all_product(database)


@router.get('/{product_id}', response_model=schema.ProductListing)
async def get_product_by_id(product_id: int, database: Session = Depends(db.get_db)):
    return await service.get_product_by_id(product_id, database)


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_product_by_id(product_id: int, database: Session = Depends(db.get_db)):
    return await service.delete_product_by_id(product_id, database)
