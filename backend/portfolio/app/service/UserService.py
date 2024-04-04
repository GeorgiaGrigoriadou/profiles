from typing import List, Type
from sqlalchemy.orm import Session
from sqlalchemy.testing import db

from app.model import models
from app.model.models import User
from app.schema import UserSchema
from app.database import get_db


class UserService:
    def __init__(self):
        pass

    def create_user(self, db, user: UserSchema.UserCreate):
        db_user = models.User(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_users(self, db):
        return db.query(models.User).all()

    def get_user_by_id(self, db, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    def update_user(self, db, user_id: int, user: UserSchema.UserCreate):
        db_user = self.get_user_by_id(db, user_id)
        if db_user:
            for attr, value in user.dict().items():
                setattr(db_user, attr, value)
            db.commit()
            db.refresh(db_user)
        return db_user

    def delete_user(self, db, user_id: int):
        db_user = self.get_user_by_id(db, user_id)
        if db_user:
            db.delete(db_user)
            db.commit()
        return db_user
