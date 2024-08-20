from typing import List, Optional
from ..database import get_db
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from fastapi import Response, status, HTTPException, Depends, APIRouter
# from sqlalchemy import func

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
def add_items(item: schemas.ItemCreate, db: Session = Depends(get_db),
              current_admin: int = Depends(oauth2.get_current_admin)):
    try:
        new_item = models.Item(added_by=current_admin.id, **item.model_dump())
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    except Exception as e:
        print(f"{e}")
        raise HTTPException(status_code=status.HTTP_226_IM_USED,
                            detail=f"Item with name: [{item.title}] already exists")


@router.get("/{id}", response_model=schemas.ItemBase)
def get_item(id: int, db: Session = Depends(get_db)):

    item = db.query(models.Item).filter(id == models.Item.id).first()

    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item with id: {id} was not found")
    return item


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id: int, db: Session = Depends(get_db), current_admin: int = Depends(oauth2.get_current_admin)):
    item_query = db.query(models.Item).filter(id == models.Item.id)
    item = item_query.first()

    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item with id: {id} does not exist")

    item_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.ItemBase)
def update_item(id: int, updated_item: schemas.ItemCreate, db: Session = Depends(get_db),
                current_admin: int = Depends(oauth2.get_current_admin)):
    item_query = db.query(models.Item).filter(id == models.Item.id)
    item = item_query.first()

    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item with id: {id} does not exist")

    item_query.update(updated_item.model_dump(), synchronize_session=False)
    db.commit()

    return item_query.first()
