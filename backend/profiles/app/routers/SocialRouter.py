from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import SocialCrud
from app.model import models
from app.schema import SocialSchema

router = APIRouter()


# CREATE
@router.post("/social/{user_id}", response_model=SocialSchema.SocialBase)
def create_social(social: SocialSchema.SocialCreate, user_id: int, db: Session = Depends(get_db)):
    return SocialCrud.create_social(db, social, user_id)


# READ ALL skills
@router.get("/socials")
def read_social(db: Session = Depends(get_db)):
    return SocialCrud.get_social(db)


# READ Skill ID
@router.get("/social/{social_id}", response_model=SocialSchema.SocialBase)
def read_social_by_id(social_id: int, db: Session = Depends(get_db)):
    db_social = SocialCrud.get_social_by_id(db, social_id)
    if db_social is None:
        raise HTTPException(status_code=404, detail="social not found")
    return db_social


@router.get("/social/{user_id}/allsocials", response_model=SocialSchema.SocialByUser)
def get_user_with_social(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(models.User, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="social not found")
    return db_user


@router.put("/social/{social_id}", response_model=SocialSchema.SocialBase)
def update_social(social_id: int, social: SocialSchema.SocialCreate, db: Session = Depends(get_db)):
    db_social = SocialCrud.get_social_by_id(db, social_id)
    if db_social is None:
        raise HTTPException(status_code=404, detail="social not found")
    return SocialCrud.update_social(db, social_id, social)


@router.delete("/social/{social_id}", response_model=None)
def delete_social(social_id: int, db: Session = Depends(get_db)):
    db_social = SocialCrud.get_social_by_id(db, social_id)
    if db_social is None:
        raise HTTPException(status_code=404, detail="social not found")
    SocialCrud.delete_social(db, social_id)
    return None
