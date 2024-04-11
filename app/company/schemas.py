from pydantic import BaseModel
from typing import Optional,List
from fastapi import HTTPException

#response model
class ShowCompanies(BaseModel):
    id: int
    company_name: str
    phone_number: str
    mobile: str
    fax: str
    sub_city: str
    business_type: str
    location: str
    url: Optional[str]
    primary_category: str
    categories: str

    class Config():
        orm_mode = True

#request Model for edit
class RequestCompanies(BaseModel):
    company_name: Optional[str] = None
    phone_number: Optional[str] = None
    mobile: Optional[str] = None
    fax: Optional[str] = None
    sub_city: Optional[str] = None
    business_type: Optional[str] = None
    location: Optional[str] = None
    url: Optional[str]
    primary_category: Optional[str] = None
    categories: Optional[str] = None

    class Config():
        orm_mode = True


#request model 
class RequestCompInitals(BaseModel):
    company_name:Optional[str] = None
    sub_city:Optional[str] = None
    business_type:Optional[str] = None
    primary_category:Optional[str] = None
    categories:Optional[str] = None

    class Config():
        orm_mode = True


#request model to get with phone no
class RequestPhone(BaseModel):
    phone_number:Optional[str] = None
    limit:int

    class Config():
        orm_mode = True

#request model to get wth mobile no
class RequestMobile(BaseModel):
    mobile:Optional[str] = None
    limit:int

    class Config():
        orm_mode = True


#request model to get with the company 
class RequestCompany(BaseModel):
    categories:Optional[str] = None
    limit:int

    class Config():
        orm_mode = True

#request model for register company
class RegisterCompany(BaseModel):
    company_name: str
    phone_number: str
    mobile: Optional[str] = None
    fax: Optional[str] = None
    sub_city: str
    business_type: str
    location: str
    url: Optional[str] = None
    primary_category: str
    categories: str

    class Config():
        orm_mode = True
# #request model for a user
# class RequestUser(BaseModel):


class RequestID(BaseModel):
    id:str
    class Config():
        orm_mode = True


#response for exception
class ExceptionResponse(HTTPException):
    status:str
    message:str

    class Config():
        orm_mode = True




#user shema
class User(BaseModel):
    name:str
    email:str
    password:str
    user_limit:int
    is_admin:str

    class Config():
        orm_mode = True


class GetUser(BaseModel):
    name: Optional[str]
    email:Optional[str]
    class Config():
        orm_mode = True

#show user schemas 
class ShowUser(BaseModel):
    id:int
    name:str
    email:str
    is_admin:str
    class Config():
        orm_mode = True


class Login(BaseModel):
    username:str
    password:str

    class Config():
        orm_mode = True



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str]
    