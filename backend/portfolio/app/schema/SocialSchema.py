# schemas.py
from pydantic import BaseModel


class SocialBase(BaseModel):
    name: str
    url: str


class SocialCreate(SocialBase):
    pass


class Social(SocialBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class SocialByUser(BaseModel):
    social: list[SocialBase] = []