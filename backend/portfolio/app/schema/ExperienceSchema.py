# EducationSchema.py
from pydantic import BaseModel
from datetime import date


class ExperienceBase(BaseModel):
    job: str
    description: str
    start_at: date
    end_at: date

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ExperienceCreate(ExperienceBase):
    pass


class Experience(ExperienceBase):
    id: int
    user_id: int
    job_type_id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class ExperienceByUser(BaseModel):
    experiences: list[ExperienceBase] = []
