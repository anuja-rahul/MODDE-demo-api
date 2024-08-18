from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
# from decimal import Decimal


class ItemBase(BaseModel):
    id: int
    title: str
    description: str
    stock: int
    price: float
    img_url: str
    created_at: datetime

    class Config:
        from_attributes = True


class ItemCreate(BaseModel):
    title: str
    description: str
    stock: Optional[int]
    price: float
    img_url: Optional[str]


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
