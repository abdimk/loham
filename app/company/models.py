from sqlalchemy import Column,String,Integer
from . import database
from .database import Base


#data base model | sql alchamey model 
class Companies(database.Base):
    __tablename__ ='companies'
    id = Column(Integer, primary_key=True,index=True)
    company_name= Column(String)
    phone_number = Column(String)
    mobile = Column(String)
    fax = Column(String)
    sub_city = Column(String)
    business_type = Column(String)
    location = Column(String)
    url = Column(String)
    primary_category = Column(String)
    categories = Column(String)
    


class User(database.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    user_limit = Column(Integer)
    is_admin = Column(String)

    #blogs = relationship("Blog", back_populates="creator")



