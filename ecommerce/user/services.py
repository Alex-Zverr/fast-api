from fastapi import HTTPException, status
from ecommerce.user import models
from ecommerce.user import schema


async def new_user_registration(request: schema.User, database) -> models.User:
    new_user = models.User(name=request.name, email=request.email, password=request.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


async def all_user(database) -> list[models.User]:
    users = database.query(models.User).all()
    return users


async def get_user_by_id(user_id, database) -> models.User | None:
    user_info = database.query(models.User).get(user_id)

    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found!")

    return user_info


async def delete_user_by_id(user_id, database):
    database.query(models.User).filter(models.User.id == user_id).delete()
    database.commit()
