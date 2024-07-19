# crud.py
from sqlalchemy.orm import Session
from app.model import models
from app.schema import ExperienceSchema


def get_experience_by_id(db: Session, experience_id: int):
    return db.query(models.Experience).filter(models.Experience.id == experience_id).first()


def get_experience(db: Session):
    return db.query(models.Experience).all()


def create_experience(db: Session, experience: ExperienceSchema.ExperienceCreate, user_id: int):
    db_experience = models.Experience(**experience.dict(), user_id=user_id)
    db.add(db_experience)
    db.commit()
    db.refresh(db_experience)
    return db_experience


def update_experience(db: Session, experience_id: int, experience: ExperienceSchema.ExperienceCreate):
    db_experience = get_experience_by_id(db, experience_id)
    if db_experience:
        for attr, value in experience.dict().items():
            setattr(db_experience, attr, value)
        db.commit()
        db.refresh(db_experience)
    return db_experience


def delete_experience(db: Session, experience_id: int):
    db_experience = get_experience_by_id(db, experience_id)
    if db_experience:
        db.delete(db_experience)
        db.commit()
    return db_experience
