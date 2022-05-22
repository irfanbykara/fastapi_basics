from fastapi import FastAPI,Response,status,APIRouter,Depends, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional,List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .. import models, schemas,utils
from ..database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix = "/users",
    tags = ['Users']
)


@router.post("/",status_code=status.HTTP_201_CREATED,response_model= schemas.User)
def create_user(user:schemas.CreateUser,db: Session = Depends(get_db)):

    #Hash the password - user.password
    print('Here I am baby')
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'User with username: {user.email} already exists.')

    password = utils.hash(user.password)
    user.password = password
    new_user = models.User(
       **user.dict()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}",response_model=schemas.User)
def get_user(id:int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id: {id} was not found.')
    return user
