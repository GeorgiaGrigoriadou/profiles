from sqlalchemy.orm import Session
from app.model import models
from app.schema import ProjectSchema


def get_project_by_id(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def get_project(db: Session):
    return db.query(models.Project).all()


def create_project(db: Session, project: ProjectSchema.ProjectCreate, user_id: int):
    db_project = models.Project(**project.dict(), user_id=user_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def update_project(db: Session, project_id: int, project: ProjectSchema.ProjectCreate):
    db_project = get_project_by_id(db, project_id)
    if db_project:
        for attr, value in project.dict().items():
            setattr(db_project, attr, value)
        db.commit()
        db.refresh(db_project)
    return db_project


def delete_project(db: Session, project_id: int):
    db_project = get_project_by_id(db, project_id)
    if db_project:
        db.delete(db_project)
        db.commit()
    return db_project
