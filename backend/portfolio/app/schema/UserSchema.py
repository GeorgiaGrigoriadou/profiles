# schemas.py

from pydantic import BaseModel, ConfigDict
from app.schema import SkillSchema
from app.schema import ProjectSchema
from app.schema import EducationSchema
from app.schema import SocialSchema
from app.schema import ExperienceSchema
from app.model.models import Skill
from app.model.models import Project
from app.model.models import Education
from app.model.models import Experience
from app.model.models import Social


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
    skills: list[Skill] = []
    projects: list[Project] = []
    education: list[Education] = []
    social: list[Social] = []
    experiences: list[Experience] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserWithSkills(UserBase):
    skills: list[SkillSchema.SkillBase] = []


class UserWithProjects(UserBase):
    projects: list[ProjectSchema.ProjectBase] = []


class UserWithEducation(UserBase):
    education: list[EducationSchema.EducationBase] = []


class UserWithSocial(UserBase):
    social: list[SocialSchema.SocialBase] = []


class UserWithExperience(UserBase):
    experience: list[ExperienceSchema.ExperienceBase] = []


class UserWithAll(UserBase):
    skills: list[SkillSchema.SkillBase] = []
    projects: list[ProjectSchema.ProjectBase] = []
    education: list[EducationSchema.EducationBase] = []
    experience: list[ExperienceSchema.ExperienceBase] = []
    social: list[SocialSchema.SocialBase] = []
