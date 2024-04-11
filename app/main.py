from fastapi import FastAPI,Depends,Response
from fastapi.responses import RedirectResponse
#import app.company.database as database
#import app.company.schemas as schemas
from .company import models
#from typing import List, Optional, Union
#from sqlalchemy.orm import Session
#from sqlalchemy import or_
#from sqlalchemy import text
#import re
from .company.routers import comp,users,auth
from .company.database import engine


app = FastAPI()
models.Base.metadata.create_all(engine)


app.include_router(auth.router)
app.include_router(comp.router)
app.include_router(users.router)




@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse('/docs')


























# from passlib.context import CryptContext
# from fastapi import FastAPI, HTTPException, Request
# from fastapi import status, HTTPException, Depends
# from fastapi.responses import RedirectResponse
# from fastapi.responses import HTMLResponse, JSONResponse
# import app.company.database as database
# import app.company.schemas as schemas
# import app.company.models as models
# from typing import List, Optional, Union
# from sqlalchemy.orm import Session
# from sqlalchemy import or_
# from sqlalchemy import text
# import re


# app = FastAPI()


# def get_db():
#     db = database.SesstionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.exception_handler(404)
# async def custom_404_handler(_, __):
#     return RedirectResponse('/docs')


# @app.get('/v1/about')
# def get_catagories():
#     return {
#         'Version': '0.0.1',
#         'Developer': 'Abdisa (Netkas) | (0_0)',
#         'Released Year': 'April 10 2024'
#     }


# @app.get("/get_me")
# async def get_me(request: Request):
#     client_ip = request.client.host
#     user_agent = request.headers["user-agent"]
#     method = request.method
#     path = request.url.path
#     query_params = request.query_params
#     cookies = request.cookies

#     return {
#         "client_ip": client_ip,
#         "user_agent": user_agent,
#         "method": method,
#         "path": path,
#         "query_params": query_params,
#         "cookies": cookies,
#         "hobo": ":)"
#     }


# @app.get('/get_category_count')
# def get_category_count(db: Session = Depends(get_db)):
#     query = text(
#         """SELECT categories, COUNT(*) AS category_count FROM companies GROUP BY categories""")
#     result = db.execute(query)
#     rows = result.fetchall()
#     category_counts_list = [{"categories": row[0],
#                              "category_count": row[1]} for row in rows]
#     return category_counts_list


# @app.get('/get/{id}', status_code=status.HTTP_200_OK)
# def get_company_with_id(id: str, request: Request, db: Session = Depends(get_db)):
#     result = db.query(models.Companies).filter(
#         models.Companies.id == id).first()
#     if not result:
#         headers = {"X-Custom-Header": "Value",
#                    "method": request.method,
#                    "path": request.url.path}
#         return HTTPException(status.HTTP_404_NOT_FOUND, detail='notfound!', headers=headers)
#     return schemas.ShowCompanies(
#         id=result.id,
#         company_name=result.company_name,
#         phone_number=result.phone_number,
#         mobile=result.mobile,
#         fax=result.fax,
#         sub_city=result.sub_city,
#         business_type=result.business_type,
#         location=result.location,
#         url=result.url,
#         primary_category=result.primary_category,
#         categories=result.categories
#     )


# @app.get('/get_with_initals/{initals}', response_model=List[schemas.ShowCompanies])
# def get_with_initals(initals: str, db: Session = Depends(get_db)):
#     result = db.query(models.Companies).filter(
#         models.Companies.company_name.like(f'%{initals}%')).limit(10).all()
#     return result


# # post request
# @app.post('/get_with_initals', response_model=List[schemas.ShowCompanies])
# def get_with_inital(request: schemas.RequestCompInitals, db: Session = Depends(get_db)):

#     query = db.query(models.Companies)
#     filters = []

#     if request.company_name:
#         filters.append(models.Companies.company_name.like(
#             f'{request.company_name}%'))
#     if request.sub_city:
#         filters.append(models.Companies.sub_city.like(f'%{request.sub_city}%'))
#     if request.business_type:
#         filters.append(models.Companies.business_type.like(
#             f'%{request.business_type}%'))
#     if request.primary_category:
#         filters.append(models.Companies.primary_category.like(
#             f'%{request.primary_category}%'))
#     if request.categories:
#         filters.append(models.Companies.categories.like(
#             f'%{request.categories}%'))

#     if filters:
#         query = query.filter(*filters)

#     return query.limit(50).all()


# def clean_phone_number(number):
#     return re.sub(r'\D', '', number)


# # improvement required
# @app.post('/get_with_phone')
# def get_with_phone(request: schemas.RequestPhone, db: Session = Depends(get_db)):
#     # phone_number_pattern = "%1161%"
#     phone_number_pattern = f"%{request.phone_number.strip(' ')}%"
#     cleaned_rows = []
#     general_query = text(
#         f"""SELECT * FROM companies WHERE phone_number LIKE :phone_number_pattern LIMIT {request.limit}""")
#     result = db.execute(
#         general_query, {"phone_number_pattern": phone_number_pattern})

#     rows = result.fetchall()

#     for row in rows:
#         cleaned_row = list(row)
#         cleaned_row[2] = row[2][: len(
#             row[2]) - len(re.sub(r'\d', '', row[2]))]  # Extract digits

#         mobile_numbers = row[3].split(',')
#         cleaned_mobile_numbers = [clean_phone_number(
#             number) for number in mobile_numbers]
#         cleaned_row[3] = ','.join(cleaned_mobile_numbers)
#         cleaned_rows.append(cleaned_row)
#     response_data = {"companies": cleaned_rows}
#     return response_data

# # improvement required


# @app.post('/get_with_mobile')
# def get_with_mobile(request: schemas.RequestMobile, db: Session = Depends(get_db)):
#     mobile_number_pattern = f"%{request.mobile.strip(' ')}%"
#     cleaned_rows = []
#     general_query = text(
#         f"""SELECT * FROM companies WHERE phone_number LIKE :phone_number_pattern LIMIT {request.limit}""")
#     result = db.execute(
#         general_query, {"phone_number_pattern": mobile_number_pattern})

#     rows = result.fetchall()
#     # Iterate through rows and clean phone numbers
#     for row in rows:
#         cleaned_row = list(row)
#         cleaned_row[2] = row[2][: len(row[2]) - len(re.sub(r'\d', '', row[2]))]

#         mobile_numbers = row[3].split(',')
#         cleaned_mobile_numbers = [clean_phone_number(
#             number) for number in mobile_numbers]
#         cleaned_row[3] = ','.join(cleaned_mobile_numbers)
#         cleaned_rows.append(cleaned_row)
#     response_data = {"companies": cleaned_rows}
#     return response_data


# @app.post('/get_with_category/{category}', response_model=List[schemas.ShowCompanies])
# def get_with_category(request: schemas.RequestCompany, db: Session = Depends(get_db)):
#     try:
#         query = db.query(models.Companies).filter(
#             models.Companies.categories == request.categories).limit(request.limit).all()
#     except:
#         query = db.query(models.Companies.like(
#             f'%{request.categories}%')).limit(request.limit).all()

#     if not query:
#         pass
#     return query


# @app.put('/update/{id}')
# def update_campanies_info(id: int, request: schemas.RequestCompanies, db: Session = Depends(get_db)):
#     query = db.query(models.Companies).filters(
#         models.Companies.id == id).first()

#     if not query:
#         pass
#     query.update({request})
#     query.commit()
#     return 'Updated Sucessfully!'


# @app.put('/register', status_code=status.HTTP_201_CREATED)
# def register_company(request: schemas.RegisterCompany, db: Session = Depends(get_db)):
#     new_data = models.Companies(
#         company_name=request.company_name,
#         phone_number=request.phone_number,
#         mobile=request.mobile,
#         fax=request.fax,
#         sub_city=request.sub_city,
#         business_type=request.business_type,
#         location=request.location,
#         url=request.url,
#         primary_category=request.primary_category,
#         categories=request.categories
#     )
#     db.add(new_data)
#     db.commit()
#     db.refresh(new_data)
#     return new_data


# @app.delete('/remove/{id}')
# def remove_company(id: str, db: Session = Depends(get_db)):
#     result = db.query(models.Companies).filter(
#         models.Companies.id == id).first()
#     if not result:
#         return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Company with the an {id} is not found!')
#     result.delete(synchronize_session=False)
#     db.commit()
#     return f'Record with an {id} has been delted Sucessfully!'


# #############################
# # User part
# ############################


# @app.post('/user',response_model=List[schemas.GetUser])
# def get_user(request: schemas.GetUser, db: Session = Depends(get_db)):
#     query = db.query(models.User)
#     filters = []

#     if request.name:
#         filters.append(models.User.name.like(f"{request.name}%"))
#     if request.email:
#         filters.append(models.User.email.like(f"{request.email}%"))

#     if filters:
#         query = query.filter(*filters)

#     return query.limit(50).all()


# pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")


# @app.post('/create_user', response_model=schemas.ShowUser)
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     hashedPassword = pwd_cxt.hash(request.password)
#     new_user = models.User(
#         name=request.name, 
#         email=request.email, 
#         password=hashedPassword, 
#         user_limit=request.user_limit,
#         is_admin=request.is_admin)
    
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)


#     return new_user

# @app.get('/get_all_users',response_model=List[schemas.ShowUser])
# def get_users(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     return users


# @app.delete('/remove_user/{id}')
# def remove_user(id:int, db : Session = Depends(get_db)):
#     query = db.query(models.User).filter(models.User.id == id)
#     if not query.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user is not found!')
#     query.delete(synchronize_session=False)
#     db.commit()
#     return f'user with an id {id} has been deleted!'
