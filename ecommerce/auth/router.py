from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestFormStrict
from sqlalchemy.orm import Session


from ecommerce import db
from ecommerce.user import hashing
from ecommerce.user.models import User

router = APIRouter(tags=["auth"])


@router.post('/login')
def login():
    pass
