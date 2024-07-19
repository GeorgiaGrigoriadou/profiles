from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import JobTypeCrud
from app.schema import JobTypeSchema

router = APIRouter()


# CREATE
@router.post("/job_type/{user_id}", response_model=JobTypeSchema.JobTypeBase)
def create_job_type(job_type: JobTypeSchema.JobTypeCreate, user_id: int, db: Session = Depends(get_db)):
    return JobTypeCrud.create_job_type(db, job_type, user_id)


# READ ALL job_types
@router.get("/job_types")
def read_job_types(db: Session = Depends(get_db)):
    return JobTypeCrud.get_job_type(db)


# READ job_type ID
@router.get("/job_type/{job_type_id}", response_model=JobTypeSchema.JobTypeBase)
def read_job_type_by_id(job_type_id: int, db: Session = Depends(get_db)):
    db_job_type = JobTypeCrud.get_job_type_by_id(db, job_type_id)
    if db_job_type is None:
        raise HTTPException(status_code=404, detail="job_type not found")
    return db_job_type


@router.put("/job_type/{job_type_id}", response_model=JobTypeSchema.JobTypeBase)
def update_job_type(job_type_id: int, job_type: JobTypeSchema.JobTypeCreate, db: Session = Depends(get_db)):
    db_job_type = JobTypeCrud.get_job_type_by_id(db, job_type_id)
    if db_job_type is None:
        raise HTTPException(status_code=404, detail="job_type not found")
    return JobTypeCrud.update_job_type(db, job_type_id, job_type)


@router.delete("/job_type/{job_type_id}", response_model=None)
def delete_job_type(job_type_id: int, db: Session = Depends(get_db)):
    db_job_type = JobTypeCrud.get_job_type_by_id(db, job_type_id)
    if db_job_type is None:
        raise HTTPException(status_code=404, detail="job_type not found")
    JobTypeCrud.delete_job_type(db, job_type_id)
    return None
