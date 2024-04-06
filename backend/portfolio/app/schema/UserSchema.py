# schemas.py

from pydantic import BaseModel, ConfigDict
from app.schema import SkillSchema
from app.schema import ProjectSchema
from app.schema import EducationSchema
from app.model.models import Skill
from app.model.models import Project
from app.model.models import Education


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
    projects: list[Project] = []
    educations: list[Education] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserWithSkills(UserBase):
    skills: list[SkillSchema.SkillBase] = []


class UserWithProjects(UserBase):
    projects: list[ProjectSchema.ProjectBase] = []


class UserWithEducation(UserBase):
    education: list[EducationSchema.EducationBase] = []

# projects: list[models.Project] = []

#
# experiences: list[models.Experience] = []
# social_profiles: list[models.SocialProfile] = []
