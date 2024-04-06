# schemas.py

from pydantic import BaseModel, PydanticUserError
from app.model.models import User


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

