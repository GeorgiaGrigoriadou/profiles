# EducationSchema.py
from pydantic import BaseModel
from app.model.models import Experience


class JobTypeBase(BaseModel):
    name: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class JobTypeCreate(JobTypeBase):
    pass


class JobType(JobTypeBase):
    id: int
    experiences: list[Experience] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
