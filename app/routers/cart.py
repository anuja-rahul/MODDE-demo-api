from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils, oauth2
from ..database import get_db
from ..config import settings
from typing import List

router = APIRouter(
    prefix="/carts",
    tags=["Carts"]
)


@router.get("/", response_model=schemas.CartOut, status_code=status.HTTP_200_OK)
def get_cart(db: Session = Depends(get_db), user: int = Depends(oauth2.get_current_user)):
    cart = db.query(models.Cart).filter(models.Cart.user_id == user.id).first()
    if not cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Cart for user [{user.id}] not found")
    cart_items = db.query(models.CartItem).filter(models.CartItem.id == cart.id).all()
    # print(cart.id)
    return {
        "id": cart.id,
        "user_id": cart.user_id,
        "created_at": cart.created_at,
        "items": cart_items
    }


@router.put("/items", response_model=schemas.CartBase, status_code=status.HTTP_200_OK)
def update_cart(updated_items: schemas.CartItemCreate, db: Session = Depends(get_db),
                user: int = Depends(oauth2.get_current_user)):
    cart = db.query(models.Cart).filter(models.Cart.user_id == user.id).first()
    cart_id = cart.id
    if not cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Cart for user [{user.id}] not found")

    cart_item_query = db.query(models.CartItem).filter(cart.id == models.CartItem.id,
                                                       updated_items.item_id == models.CartItem.item_id)
    cart_item = cart_item_query.first()

    if cart_item is None:
        new_item = models.CartItem(id=cart_id, **updated_items.model_dump())
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    else:
        cart_item_query.update(updated_items.model_dump())
