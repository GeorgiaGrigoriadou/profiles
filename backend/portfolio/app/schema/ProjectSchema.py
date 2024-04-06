# schemas.py

from pydantic import BaseModel, ConfigDict


class ProjectBase(BaseModel):
    name: str
    image: str
    description: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int
    user_id: int  # Add user_id field

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ProjectByUser(BaseModel):
    projects: list[ProjectBase] = []

# projects: list[models.Project] = []

# educations: list[models.Education] = []
# experiences: list[models.Experience] = []
# social_profiles: list[models.SocialProfile] = []
