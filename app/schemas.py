from typing import Optional, Literal
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
    discount: Optional[int]
    gender: Literal["male", "female", "unisex"]
    type: Literal["top", "bottom"]
    created_at: datetime
    added_by: int

    class Config:
        from_attributes = True


class ItemCreate(BaseModel):
    title: str
    description: str
    stock: Optional[int]
    price: float
    img_url: Optional[str]
    gender: Literal["male", "female", "unisex"]
    type: Literal["top", "bottom"]


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


# class UserUpdate(BaseModel):
#     name: Optional[str]
#     email: Optional[EmailStr]
#     password: Optional[str]


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    verified: bool
    created_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class CartBase(BaseModel):
    id: int
    user_id: int
    created_at: datetime


class AdminCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class AdminOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class AdminLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
