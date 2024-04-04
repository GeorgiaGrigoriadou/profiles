# EducationSchema.py
from pydantic import BaseModel
from datetime import date


class EducationBase(BaseModel):
    organization: str
    image: str
    description: str
    start_at: date
    end_at: date


class EducationCreate(EducationBase):
    pass


class EducationUpdate(EducationBase):
    pass


class Education(EducationBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
