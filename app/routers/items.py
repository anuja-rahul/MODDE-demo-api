from typing import List, Optional
from ..database import get_db
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import Response, status, HTTPException, Depends, APIRouter

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


@router.get("/", response_model=List[schemas.ItemBase])
def get_items(db: Session = Depends(get_db), limit: int = 10, offset: int = 0, search: Optional[str] = ""):
    results = db.query(models.Item).filter(
        models.Item.title.contains(search)).order_by(models.Item.created_at).limit(limit).offset(offset).all()
    return results


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ItemBase)
def add_items(item: schemas.ItemCreate, db: Session = Depends(get_db)):

    new_item = models.Item(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item
