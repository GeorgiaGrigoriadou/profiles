from app.model import *
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    firstname = Column(String)
    lastname = Column(String)
    about = Column(String)
    phone = Column(String)
    email = Column(String)

    skills = relationship("Skill", back_populates="user")
    projects = relationship("Project", back_populates="user")
    education = relationship("Education", back_populates="user")
    social = relationship("Social", back_populates="user")
    experiences = relationship("Experience", back_populates="user")


class Skill(Base):
    __tablename__ = 'skill'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="skills")


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    image = Column(String, unique=True, index=True)
    description = Column(String, unique=True, index=True)

    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="projects")


class Education(Base):
    __tablename__ = 'education'

    id = Column(Integer, primary_key=True, index=True)
    organization = Column(String, unique=True, index=True)
    description = Column(String, unique=True, index=True)
    start_at = Column(DateTime, index=True)
    end_at = Column(DateTime, index=True)

    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="education")


class Social(Base):
    __tablename__ = 'social'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    url = Column(String, unique=True, index=True)

    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="social")


class Experience(Base):
    __tablename__ = 'experience'

    id = Column(Integer, primary_key=True, index=True)
    job = Column(String, unique=True, index=True)
    description = Column(String, unique=True, index=True)
    start_at = Column(DateTime, unique=True, index=True)
    end_at = Column(DateTime, unique=True, index=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    job_type_id = Column(Integer, ForeignKey('job_type.id'))

    user = relationship("User", back_populates="experiences")
    job_type = relationship("JobType", back_populates="experiences")


class JobType(Base):
    __tablename__ = 'job_type'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    experiences = relationship("Experience", back_populates="job_type")

