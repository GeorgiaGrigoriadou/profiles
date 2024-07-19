from sqlalchemy.orm import Session
from app.model import models
from app.schema import SkillSchema


def get_skill_by_id(db: Session, skill_id: int):
    return db.query(models.Skill).filter(models.Skill.id == skill_id).first()


def get_skills(db: Session):
    return db.query(models.Skill).all()


def create_skill(db: Session, skill: SkillSchema.SkillCreate, user_id: int):
    db_skill = models.Skill(**skill.dict(), user_id=user_id)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def update_skill(db: Session, skill_id: int, skill: SkillSchema.SkillCreate):
    db_skill = get_skill_by_id(db, skill_id)
    if db_skill:
        for attr, value in skill.dict().items():
            setattr(db_skill, attr, value)
        db.commit()
        db.refresh(db_skill)
    return db_skill


def delete_skill(db: Session, skill_id: int):
    db_skill = get_skill_by_id(db, skill_id)
    if db_skill:
        db.delete(db_skill)
        db.commit()
    return db_skill
