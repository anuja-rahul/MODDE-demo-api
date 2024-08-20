from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils, oauth2
from ..database import get_db
from ..config import settings


router = APIRouter(
    prefix="/carts",
    tags=["Carts"]
)
