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
    user_id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ProjectByUser(BaseModel):
    projects: list[ProjectBase] = []

