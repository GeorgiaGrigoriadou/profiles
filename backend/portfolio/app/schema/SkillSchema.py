# schemas.py
from typing import List

from pydantic import BaseModel, PydanticUserError
from app.model.models import User
from app.model import models


class SkillBase(BaseModel):
    name: str
    description: str
    # class Config:
    #     orm_mode = True
    #     arbitrary_types_allowed = True


class SkillCreate(SkillBase):
    pass


class Skill(SkillBase):
    id: int
    user_id: int  # Add user_id field

    class Config:
        orm_mode = True


class SkillsByUser(BaseModel):
    skills: list[SkillBase] = []
