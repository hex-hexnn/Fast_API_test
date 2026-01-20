from fastapi import FastAPI
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine
from models import SQLModel
from routers import items # Importujemy nasz router

@asynccontextmanager

async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(items.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "System ready. Go to /docs to get started."}