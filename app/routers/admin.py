from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils, oauth2
from ..database import get_db


router = APIRouter(
    prefix="/admins",
    tags=["Admin Authentication"]
)


@router.post("/login", response_model=schemas.Token)
def login(admin_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    admin = db.query(models.Admin).filter(admin_credentials.username == models.Admin.email).first()

    if not admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not utils.verify(admin_credentials.password, admin.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    access_token = oauth2.create_access_token(data={"admin_id": admin.id})

    return {"access_token": access_token,
            "token_type": "bearer"}


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.AdminOut)
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):

    try:
        hashed_password = utils.hash(admin.password)
        admin.password = hashed_password
        new_admin = models.Admin(**admin.model_dump())
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
    except Exception:
        raise HTTPException(status_code=status.HTTP_226_IM_USED, detail=Exception)

    return new_admin


@router.get("/{id}", response_model=schemas.AdminOut)
def get_admin(id: int, db: Session = Depends(get_db)):
    admin = db.query(models.Admin).filter(id == models.Admin.id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"admin with id: {id} was not found")
    return admin
