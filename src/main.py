from fastapi import FastAPI

from src.api.auth import router as auth_router
from src.database.database import Base, engine

import src.database.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Project Management API",
    version="1.0.0",
)

app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Project Management API is running"
    }