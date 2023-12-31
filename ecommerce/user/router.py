from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from ecommerce import db
from ecommerce.user import schema
from ecommerce.user import services
from ecommerce.user import validator

router = APIRouter(tags=['Users'], prefix='/user')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schema.User, database: Session = Depends(db.get_db)):
    user = await validator.verify_email_exist(request.email, database)

    if user:
        raise HTTPException(
            status_code=400,
            detail='Аккаунт, использующий указанный Вами адрес электронной почты, уже существует.'
        )

    new_user = await services.new_user_registration(request, database)
    return new_user


@router.get('/', response_model=list[schema.DisplayUser])
async def get_all_user(database: Session = Depends(db.get_db)):
    return await services.all_user(database)


@router.get('/{user_id}', response_model=schema.DisplayUser)
async def get_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    return await services.get_user_by_id(user_id, database)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_user_by_id(user_id, database)
