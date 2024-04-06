from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import SkillCrud
from app.model import models
from app.schema import SkillSchema

router = APIRouter()


# CREATE
@router.post("/skill/{user_id}", response_model=SkillSchema.SkillBase)
def create_skill(skill: SkillSchema.SkillCreate, user_id: int, db: Session = Depends(get_db)):
    return SkillCrud.create_skill(db, skill, user_id)


# READ ALL skills
@router.get("/skills")
def read_skills(db: Session = Depends(get_db)):
    return SkillCrud.get_skills(db)


# READ Skill ID
@router.get("/skill/{skill_id}", response_model=SkillSchema.SkillBase)
def read_skill_by_id(skill_id: int, db: Session = Depends(get_db)):
    db_skill = SkillCrud.get_skill_by_id(db, skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return db_skill


@router.get("/skills/{user_id}/allskills", response_model=SkillSchema.SkillsByUser)
def get_user_with_skills(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(models.User, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/skill/{skill_id}", response_model=SkillSchema.SkillBase)
def update_skill(skill_id: int, skill: SkillSchema.SkillCreate, db: Session = Depends(get_db)):
    db_skill = SkillCrud.get_skill_by_id(db, skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return SkillCrud.update_skill(db, skill_id, skill)


@router.delete("/skill/{skill_id}", response_model=None)
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    db_skill = SkillCrud.delete_skill(db, skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="skill not found")
    SkillCrud.delete_skill(db, skill_id)
    return None
