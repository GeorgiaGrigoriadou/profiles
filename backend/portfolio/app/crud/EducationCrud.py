# crud.py
from sqlalchemy.orm import Session
from app.model import models
from app.schema import EducationSchema


def get_education_by_id(db: Session, education_id: int):
    return db.query(models.Education).filter(models.Education.id == education_id).first()


def get_education(db: Session):
    return db.query(models.Education).all()


def create_education(db: Session, education: EducationSchema.EducationCreate, user_id: int):
    db_education = models.Education(**education.dict(), user_id=user_id)
    db.add(db_education)
    db.commit()
    db.refresh(db_education)
    return db_education


def update_education(db: Session, education_id: int, education: EducationSchema.EducationCreate):
    db_education = get_education_by_id(db, education_id)
    if db_education:
        for attr, value in education.dict().items():
            setattr(db_education, attr, value)
        db.commit()
        db.refresh(db_education)
    return db_education


def delete_education(db: Session, education_id: int):
    db_education = get_education_by_id(db, education_id)
    if db_education:
        db.delete(db_education)
        db.commit()
    return db_education
