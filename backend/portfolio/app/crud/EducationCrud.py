# crud.py
from sqlalchemy.orm import Session
from app.model import models
from app.schema import EducationSchema


def create_education(db: Session, education: EducationSchema.EducationCreate):
    db_education = models.Education(**education.dict())
    db.add(db_education)
    db.commit()
    db.refresh(db_education)
    return db_education


def get_education(db: Session, education_id: int):
    return db.query(models.Education).filter(models.Education.id == education_id).first()


def get_all_education(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Education).offset(skip).limit(limit).all()


def find_education_by_organization(db: Session, organization: str):
    return db.query(models.Education).filter(models.Education.organization == organization).all()


def update_education(db: Session, education_id: int, education_data: EducationSchema.EducationUpdate):
    db_education = db.query(models.Education).filter(models.Education.id == education_id).first()
    if db_education:
        for key, value in education_data.dict().items():
            setattr(db_education, key, value)
        db.commit()
        db.refresh(db_education)
        return db_education
    return None


def delete_education(db: Session, education_id: int):
    db_education = db.query(models.Education).filter(models.Education.id == education_id).first()
    if db_education:
        db.delete(db_education)
        db.commit()
        return True
    return False
