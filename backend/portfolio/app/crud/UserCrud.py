from sqlalchemy.orm import Session, joinedload
from app.model import models
from app.schema import UserSchema
from app.schema import SkillSchema


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: UserSchema.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: UserSchema.UserCreate, user_id: int):
    db_user = get_user_by_id(db, user_id)
    if db_user:
        for attr, value in user.dict().items():
            setattr(db_user, attr, value)
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user_by_id(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


# def create_skill_for_user(db: Session, skill: SkillSchema.SkillCreate, user_id: int):
#     db_skill = models.Skill(**skill.dict(), user_id=user_id)
#     db.add(db_skill)
#     db.commit()
#     db.refresh(db_skill)
#     return db_skill
