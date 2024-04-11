import re
from typing import List
from fastapi import Depends
from sqlalchemy import text
from .. import oauth2
from sqlalchemy.orm import Session
from .. import schemas,models,database
from fastapi import APIRouter
from fastapi import status,Response,HTTPException,Request
from passlib.context import CryptContext
from fastapi.responses import RedirectResponse


def get_db():
    db = database.SesstionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter(
    tags=['Users']
)


#get_db = database.get_db()

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")


@router.post('/user',response_model=List[schemas.GetUser])
def get_user(request: schemas.GetUser,current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    query = db.query(models.User)
    filters = []

    if request.name:
        filters.append(models.User.name.like(f"{request.name}%"))
    if request.email:
        filters.append(models.User.email.like(f"{request.email}%"))

    if filters:
        query = query.filter(*filters)

    return query.limit(50).all()


# @router.get("/users/me")
# async def read_users_me(current_user: dict = Depends(oauth2.get_current_user)):
#     return current_user


@router.post('/create_user', response_model=schemas.ShowUser)
def create_user(request: schemas.User,current_user: schemas.User = Depends(oauth2.get_current_user),db: Session = Depends(get_db)):
    
    hashedPassword = pwd_cxt.hash(request.password)
    new_user = models.User(
        name=request.name, 
        email=request.email, 
        password=hashedPassword, 
        user_limit=request.user_limit,
        is_admin=request.is_admin)
        
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    #return f"You don't have the privilege to create user ng!"

@router.get('/get_all_users',response_model=List[schemas.ShowUser])
def get_users(current_user: schemas.User = Depends(oauth2.get_current_user),db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@router.delete('/remove_user/{id}')
def remove_user(id:int, current_user: schemas.User = Depends(oauth2.get_current_user),db : Session = Depends(get_db)):
    query = db.query(models.User).filter(models.User.id == id)
    is_admin = db.query(models.User).filter(models.User.is_admin == "Yes")
    
    if is_admin:
        return 'for real'
    
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user is not found!')
    query.delete(synchronize_session=False)
    db.commit()
    return f'user with an id {id} has been deleted!'
