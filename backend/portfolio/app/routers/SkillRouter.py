from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import UserCrud
from app.crud import SkillCrud
from app.model import models
from app.schema import UserSchema
from app.schema import SkillSchema

router = APIRouter()


# CREATE
@router.post("/skills", response_model=SkillSchema.SkillBase)
def create_skill(skill: SkillSchema.SkillCreate,  user_id: int, db: Session = Depends(get_db)):
    return SkillCrud.create_skill(db, skill)


# READ ALL skills
@router.get("/skills")
def read_skills(db: Session = Depends(get_db)):
    return SkillCrud.get_skills(db)


# READ Skill ID
@router.get("/skills/{skill_id}", response_model=SkillSchema.SkillBase)
def read_skill_by_id(skill_id: int, db: Session = Depends(get_db)):
    db_skill = SkillCrud.get_skill_by_id(db, skill_id = skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return db_skill


@router.put("/skills/{skill_id}", response_model=SkillSchema.SkillBase)
def update_skill(skill_id: int, skill: SkillSchema.SkillCreate, db: Session = Depends(get_db)):
    db_skill = SkillCrud.get_skill_by_id(db, skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return SkillCrud.update_skill(db, skill_id, skill)


@router.delete("/skills/{skill_id}", response_model=None)
def delete_user(skill_id: int, db: Session = Depends(get_db)):
    db_skill = SkillCrud.delete_skill(db, skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="User not found")
    SkillCrud.delete_skill(db, skill_id)
    return None



