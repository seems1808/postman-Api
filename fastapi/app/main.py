from fastapi import FastAPI

from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ProWorld User API",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to ProWorld FastAPI Backend"
    }
