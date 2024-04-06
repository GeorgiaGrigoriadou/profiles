from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import EducationCrud
from app.model import models
from app.schema import EducationSchema

router = APIRouter()


# CREATE
@router.post("/education/{user_id}", response_model=EducationSchema.EducationBase)
def create_education(education: EducationSchema.EducationCreate, user_id: int, db: Session = Depends(get_db)):
    return EducationCrud.create_education(db, education, user_id)


# READ ALL skills
@router.get("/educations")
def read_education(db: Session = Depends(get_db)):
    return EducationCrud.get_education(db)


# READ Skill ID
@router.get("/education/{education_id}", response_model=EducationSchema.EducationBase)
def read_project_by_id(education_id: int, db: Session = Depends(get_db)):
    db_education = EducationCrud.get_education_by_id(db, education_id)
    if db_education is None:
        raise HTTPException(status_code=404, detail="Education not found")
    return db_education


@router.get("/education/{user_id}/alleducation", response_model=EducationSchema.EducationByUser)
def get_user_with_education(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(models.User, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/education/{education_id}", response_model=EducationSchema.EducationBase)
def update_education(education_id: int, education: EducationSchema.EducationCreate, db: Session = Depends(get_db)):
    db_education = EducationCrud.get_education_by_id(db, education_id)
    if db_education is None:
        raise HTTPException(status_code=404, detail="education not found")
    return EducationCrud.update_education(db, education_id, education)


@router.delete("/education/{education_id}", response_model=None)
def delete_education(education_id: int, db: Session = Depends(get_db)):
    db_education = EducationCrud.delete_education(db, education_id)
    if db_education is None:
        raise HTTPException(status_code=404, detail="project not found")
    EducationCrud.delete_education(db, education_id)
    return None
