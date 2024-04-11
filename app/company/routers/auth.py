from fastapi import status
from sqlalchemy.orm import Session
from .. import schemas, database, models,token
from passlib.context import CryptContext
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter(
    tags=['Login']
)

def get_db():
    db = database.SesstionLocal()
    try:
        yield db
    finally:
        db.close()




pwd_cxt = CryptContext(schemes=['bcrypt'],deprecated="auto")

def verify(hashedPassword, password):
    if pwd_cxt.verify(password, hashedPassword):
        return True
    return False

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with an email of {request.username} is not found!")
    if not verify(user.password , request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"password does't match!")
        #return f"password: {user.password}, \n request:{pwd_cxt.hash(request.password)}"



    #access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    #access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}
    #return user