from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQL_ALCHEMY_DATABASE_URL = 'sqlite:///./companies.db'
#SQL_ALCHEMY_USERDATABASE_URL = 'sqlite:///./user.db'


engine = create_engine(SQL_ALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})
# user_engine = create_engine(SQL_ALCHEMY_USERDATABASE_URL, connect_args={"check_same_thread":False})

SesstionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()



