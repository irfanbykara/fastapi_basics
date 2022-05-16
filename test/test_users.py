from fastapi.testclient import TestClient
from app.main import app
from app.schemas import User
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db
from app import models
import pytest
from app import schemas
from jose import jwt
from app.config import settings



def test_root(client,session):
    res = client.get("/")
    assert res.json().get('message') == 'Benim adım Irfan Senin adın ne'
    assert res.status_code ==200


def test_create_user(client):
    res = client.post('/users/',json={
        "email":"helloworld2@software.com",
        "password" : "HelloWorld"
    })
    new_user = User(**res.json())
    assert new_user.email == "helloworld2@software.com"
    assert res.status_code == 201

def test_login_user(client,test_user):
    res = client.post('/login',data={
        "username":test_user['email'],
        "password" : test_user['password']
    })
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token,
                         settings.secret_key,
                         algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


@pytest.mark.parametrize("email,password,status_code",
                         [
                             ("xxx@gmail.com","sdfsdfdsf",403),
                             ("sdffsfdsdf@gmail.com","HelloWorld",403),
                             ("sdfsdf@gmail.com","faqbadi",403)
                         ])

def test_incorrect_login(email,password,client,status_code):
    res = client.post("/login", data = {"username":email,
                                        "password":password})
    assert res.status_code == status_code
    assert res.json().get("detail") == "Invalid Credentials"
