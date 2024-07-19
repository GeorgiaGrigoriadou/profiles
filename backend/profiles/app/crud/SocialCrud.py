from sqlalchemy.orm import Session
from app.model import models
from app.schema import SocialSchema


def get_social_by_id(db: Session, social_id: int):
    return db.query(models.Social).filter(models.Social.id == social_id).first()


def get_social(db: Session):
    return db.query(models.Social).all()


def create_social(db: Session, social: SocialSchema.SocialCreate, user_id: int):
    db_social = models.Social(**social.dict(), user_id=user_id)
    db.add(db_social)
    db.commit()
    db.refresh(db_social)
    return db_social


def update_social(db: Session, social_id: int, skill: SocialSchema.SocialCreate):
    db_social = get_social_by_id(db, social_id)
    if db_social:
        for attr, value in skill.dict().items():
            setattr(db_social, attr, value)
        db.commit()
        db.refresh(db_social)
    return db_social


def delete_social(db: Session, social_id: int):
    db_social = get_social_by_id(db, social_id)
    if db_social:
        db.delete(db_social)
        db.commit()
    return db_social
