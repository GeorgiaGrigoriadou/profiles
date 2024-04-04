from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.service.UserService import UserService
from app.schema import UserSchema
from typing import List

router = APIRouter()
service = UserService()


@router.get("/users/", response_model=List[UserSchema.User])
def read_users(db: Session = Depends(get_db)):
    return service.get_users(db)


@router.get("/users/{user_id}", response_model=UserSchema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = service.get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/users/{user_id}", response_model=None)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = service.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    service.delete_user(db, user_id)
    return None


@router.post("/users/", response_model=UserSchema.User)
def create_user(user: UserSchema.UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)


@router.put("/users/{user_id}", response_model=UserSchema.User)
def update_user(user_id: int, user: UserSchema.UserCreate, db: Session = Depends(get_db)):
    db_user = service.get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return service.update_user(db, user_id, user)
