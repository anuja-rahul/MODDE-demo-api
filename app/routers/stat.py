from typing import List, Optional
from ..database import get_db
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from fastapi import Response, status, HTTPException, Depends, APIRouter

router = APIRouter(
    prefix="/stats",
    tags=["Statistics"]
)


@router.get("/sales", response_model=List[schemas.SaleOutMin])
def get_items(db: Session = Depends(get_db), admin_user: int = Depends(oauth2.get_current_admin)):
    results = db.query(models.Sale).filter(
        models.Sale.owner_id == admin_user.id).order_by(models.Sale.updated_at).all()
    return results
