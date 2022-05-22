from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint


class UserBase(BaseModel):
    email: EmailStr
    password: str
    image_url: str
    trial_str: str

class CreateUser(UserBase):
    pass


class User(BaseModel):
    id: int
    email: EmailStr
    image_url: str
    trial_str: str
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class CreatePost(PostBase):
    pass

class Post(BaseModel):
    title: str
    content: str
    published: bool
    created_at: datetime
    owner_id: int
    owner: User

    class Config:
        orm_mode = True



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):

    post_id: int
    dir: conint(le=1)

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True
