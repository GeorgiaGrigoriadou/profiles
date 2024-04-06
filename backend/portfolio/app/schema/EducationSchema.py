# EducationSchema.py
from pydantic import BaseModel
from datetime import date


class EducationBase(BaseModel):
    organization: str
    description: str
    start_at: date
    end_at: date

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class EducationCreate(EducationBase):
    pass


class Education(EducationBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class EducationByUser(BaseModel):
    education: list[EducationBase] = []
