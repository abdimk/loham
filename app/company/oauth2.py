from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import JWTError,jwt
from . import token
from . import database,models
from sqlalchemy.orm import Session


def get_user_by_session_token(db: Session, session_token: str):
    return db.query(models.User).filter(models.User.session_token == session_token).first()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return token.verify_token(data,credentials_exception)
