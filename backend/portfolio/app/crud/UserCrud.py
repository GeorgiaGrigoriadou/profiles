from typing import List, Type
from app.model import models
from sqlalchemy.orm import Session
from app.schema import UserSchema


def create_user(db: Session, user: UserSchema.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(models.User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def update_user(db: Session, user_id: int, user: UserSchema.UserCreate):
    db_user = get_user_by_id(db, user_id)
    if db_user:
        for attr, value in user.dict().items():
            setattr(db_user, attr, value)
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int) -> None:
    db_user = get_user_by_id(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
