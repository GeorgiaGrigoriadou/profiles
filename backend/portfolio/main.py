#main.py
from fastapi import FastAPI
from app.model import models
from app import database
from app.routers import UserRouter
import uvicorn


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(UserRouter.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
