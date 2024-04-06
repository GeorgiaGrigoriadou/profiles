# schemas.py

from pydantic import BaseModel, ConfigDict
from app.schema import SkillSchema
from app.model.models import Skill


class UserBase(BaseModel):
    firstname: str
    lastname: str
    about: str
    phone: str
    email: str

    # skills: list[SkillSchema.SkillBase] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    skills: list[Skill] = []  # Include skills field of type List[Skill]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserWithSkills(UserBase):
    skills: list[SkillSchema.SkillBase] = []


# projects: list[models.Project] = []

# educations: list[models.Education] = []
# experiences: list[models.Experience] = []
# social_profiles: list[models.SocialProfile] = []
