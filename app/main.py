from fastapi import FastAPI,Response,status,Depends, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional,List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas,utils
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from .routers import post,user,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


#This is not required if you use alembic.
#Just keeping it for instructive purposes.

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

#Middleware basically a function that runs before every request.

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)




@app.get("/")
async def root():
    return {'message':'Benim adım Irfan Senin adın ne'}

