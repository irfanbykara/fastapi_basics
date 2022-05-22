from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    print('I am loggin in thourgh the front-end brah...')
    user = db.query(models.User).filter(
        models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    # create a token
    # return token

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}

@router.get('/logout',)
def logout(token:str = Depends(oauth2.get_current_user_token), db: Session = Depends(database.get_db),):
    print('Inside the func...')
    response = RedirectResponse('/login', status_code=302)

    response.delete_cookie("access_token")

    print(token)
    added_token = models.BlackListTokens(

        token=token
    )
    db.add(added_token)
    db.commit()
    db.refresh(added_token)

    return {'message': f'you successfully blacklisted the token:{token}'}


