from fastapi import FastAPI
from .db import database, models
from .api import endpoints

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(endpoints.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API"}
