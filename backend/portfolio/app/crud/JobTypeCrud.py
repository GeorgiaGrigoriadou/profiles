from sqlalchemy.orm import Session
from app.model import models
from app.schema import JobTypeSchema


def get_job_type_by_id(db: Session, job_type_id: int):
    return db.query(models.JobType).filter(models.JobType.id == job_type_id).first()


def get_job_type(db: Session):
    return db.query(models.JobType).all()


def create_job_type(db: Session, job_type_id: JobTypeSchema.JobTypeCreate, user_id: int):
    db_job_type = models.JobType(**job_type_id.dict(), user_id=user_id)
    db.add(db_job_type)
    db.commit()
    db.refresh(db_job_type)
    return db_job_type


def update_job_type(db: Session, job_type_id: int, job_type: JobTypeSchema.JobTypeCreate):
    db_job_type = get_job_type_by_id(db, job_type_id)
    if db_job_type:
        for attr, value in job_type.dict().items():
            setattr(db_job_type, attr, value)
        db.commit()
        db.refresh(db_job_type)
    return db_job_type


def delete_job_type(db: Session, job_type_id: int):
    db_job_type = get_job_type_by_id(db, job_type_id)
    if db_job_type:
        db.delete(db_job_type)
        db.commit()
    return db_job_type
