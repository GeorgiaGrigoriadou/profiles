# main.py
from fastapi import FastAPI

from app.database import SessionLocal
from app.model import models
from app import database
from app.routers import UserRouter
from app.routers import SkillRouter
from app.routers import ProjectRouter
from app.routers import EducationRouter
from app.routers import SocialRouter

import uvicorn

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


app.include_router(UserRouter.router)
app.include_router(SkillRouter.router)
app.include_router(ProjectRouter.router)
app.include_router(EducationRouter.router)
app.include_router(SocialRouter.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
