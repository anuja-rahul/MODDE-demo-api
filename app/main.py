from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import items, admin, users, auth
from . import models
from .database import engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="MODDE-API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

origins = ["*"]

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router)
app.include_router(admin.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "This is the MODDE demo API"}
