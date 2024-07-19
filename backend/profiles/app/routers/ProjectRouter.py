from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import ProjectCrud
from app.model import models
from app.schema import ProjectSchema

router = APIRouter()


# CREATE
@router.post("/project/{user_id}", response_model=ProjectSchema.ProjectBase)
def create_project(project: ProjectSchema.ProjectCreate, user_id: int, db: Session = Depends(get_db)):
    return ProjectCrud.create_project(db, project, user_id)


# READ ALL skills
@router.get("/projects")
def read_project(db: Session = Depends(get_db)):
    return ProjectCrud.get_project(db)


# READ Skill ID
@router.get("/project/{project_id}", response_model=ProjectSchema.ProjectBase)
def read_project_by_id(project_id: int, db: Session = Depends(get_db)):
    db_project = ProjectCrud.get_project_by_id(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


@router.get("/projects/{user_id}/allprojects", response_model=ProjectSchema.ProjectByUser)
def get_user_with_projects(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(models.User, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/project/{project_id}", response_model=ProjectSchema.ProjectBase)
def update_project(project_id: int, project: ProjectSchema.ProjectCreate, db: Session = Depends(get_db)):
    db_project = ProjectCrud.get_project_by_id(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="project not found")
    return ProjectCrud.update_project(db, project_id, project)


@router.delete("/project/{project_id}", response_model=None)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    db_project = ProjectCrud.get_project_by_id(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="project not found")
    ProjectCrud.delete_project(db, project_id)
    return None
