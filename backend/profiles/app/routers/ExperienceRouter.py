from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import ExperienceCrud
from app.model import models
from app.schema import ExperienceSchema

router = APIRouter()


# CREATE
@router.post("/experience/{user_id}", response_model=ExperienceSchema.ExperienceBase)
def create_experience(experience: ExperienceSchema.ExperienceCreate, user_id: int, db: Session = Depends(get_db)):
    return ExperienceCrud.create_experience(db, experience, user_id)


# READ ALL skills
@router.get("/experiences")
def read_experience(db: Session = Depends(get_db)):
    return ExperienceCrud.get_experience(db)


# READ Skill ID
@router.get("/experience/{experience_id}", response_model=ExperienceSchema.ExperienceBase)
def read_project_by_id(experience_id: int, db: Session = Depends(get_db)):
    db_experience = ExperienceCrud.get_experience_by_id(db, experience_id)
    if db_experience is None:
        raise HTTPException(status_code=404, detail="experience not found")
    return db_experience


@router.get("/experience/{user_id}/allexperience", response_model=ExperienceSchema.ExperienceByUser)
def get_user_with_experience(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(models.User, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/experience/{experience_id}", response_model=ExperienceSchema.ExperienceCreate)
def update_experience(experience_id: int, experience: ExperienceSchema.ExperienceCreate, db: Session = Depends(get_db)):
    db_experience = ExperienceCrud.get_experience_by_id(db, experience_id)
    if db_experience is None:
        raise HTTPException(status_code=404, detail="experience not found")
    return ExperienceCrud.update_experience(db, experience_id, experience)


@router.delete("/experience/{experience_id}", response_model=None)
def delete_experience(experience_id: int, db: Session = Depends(get_db)):
    db_experience = ExperienceCrud.get_experience_by_id(db, experience_id)
    if db_experience is None:
        raise HTTPException(status_code=404, detail="project not found")
    ExperienceCrud.delete_experience(db, experience_id)
    return None
