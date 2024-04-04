# schemas.py

from pydantic import BaseModel
from typing import Optional
from app.model import models


class UserBase(BaseModel):
    firstname: str
    lastname: str
    about: str
    phone: str
    email: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    # projects: list[models.Project] = []
    # skills: list[models.Skill] = []
    # educations: list[models.Education] = []
    # experiences: list[models.Experience] = []
    # social_profiles: list[models.SocialProfile] = []

    class Config:
        orm_mode = True
