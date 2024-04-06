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
@router.post("/users", response_model=UserSchema.UserBase)
def create_user(user: UserSchema.UserCreate, db: Session = Depends(get_db)):
    return UserCrud.create_user(db, user)


# READ ALL USERS
@router.get("/users")
def read_users(db: Session = Depends(get_db)):
    return UserCrud.get_users(db)


# READ USER ID
@router.get("/users/{user_id}", response_model=UserSchema.UserBase)
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = UserCrud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/users/{user_id}", response_model=UserSchema.UserBase)
def update_user(user_id: int, user: UserSchema.UserCreate, db: Session = Depends(get_db)):
    db_user = UserCrud.get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserCrud.update_user(db, user_id, user)


@router.delete("/users/{user_id}", response_model=None)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserCrud.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    UserCrud.delete_user(db, user_id)
    return None


################### SKILL ###########################################
@router.get("/users/{user_id}/allskills", response_model=UserSchema.UserWithSkills)
def get_user_with_skills(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(models.User, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# CREATE SKILL FOR USER
@router.post("/users/{user_id}/skill", response_model=SkillSchema.SkillCreate)
def create_skill_for_user(user_id: int, skill: SkillSchema.SkillCreate, db: Session = Depends(get_db)):
    db_skill = SkillCrud.create_skill(db=db, skill=skill, user_id=user_id)
    return db_skill
