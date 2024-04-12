from fastapi import FastAPI,Depends,Response
from fastapi.responses import RedirectResponse
from company import models
from company.routers import comp,users,auth
from company.database import engine


app = FastAPI(redoc_url=None)
models.Base.metadata.create_all(engine)


app.include_router(auth.router)
app.include_router(comp.router)
app.include_router(users.router)




@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse('/docs')
