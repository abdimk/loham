import sys
from fastapi import FastAPI,Depends,Response
from fastapi.responses import RedirectResponse
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from .company.database import engine
from .company.routers import comp,users,auth
from .company import models


app = FastAPI(redoc_url=None)
models.Base.metadata.create_all(engine)


app.include_router(auth.router)
app.include_router(comp.router)
app.include_router(users.router)




@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse('/docs')
