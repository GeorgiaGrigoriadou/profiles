# # routers/education.py
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from app.schema import EducationSchema
# from app.service import EducationService
# from app import database
#
# router = APIRouter(prefix="/education", tags=["Education"])
#
# get_db = Database.get_db
#
#
# @router.post("/", response_model=EducationSchema.Education)
# def create_education(education: EducationSchema.EducationCreate, db: Session = Depends(get_db)):
#     education_service = EducationService(db)
#     return education_service.create_education(education)
#
#
# @router.get("/{education_id}", response_model=EducationSchema.Education)
# def get_education(education_id: int, db: Session = Depends(get_db)):
#     education_service = EducationService(db)
#     db_education = education_service.get_education(education_id)
#     if db_education is None:
#         raise HTTPException(status_code=404, detail="Education not found")
#     return db_education
#
#
# @router.get("/", response_model=List[EducationSchema.Education])
# def get_all_education(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     education_service = EducationService(db)
#     return education_service.get_all_education(skip, limit)
#
#
# @router.get("/search/", response_model=List[EducationSchema.Education])
# def find_education_by_organization(organization: str, db: Session = Depends(get_db)):
#     education_service = EducationService(db)
#     return education_service.find_education_by_organization(organization)
#
#
# @router.put("/{education_id}", response_model=EducationSchema.Education)
# def update_education(education_id: int, education: EducationSchema.EducationUpdate, db: Session = Depends(get_db)):
#     education_service = EducationService(db)
#     updated_education = education_service.update_education(education_id, education)
#     if updated_education is None:
#         raise HTTPException(status_code=404, detail="Education not found")
#     return updated_education
#
#
# @router.delete("/{education_id}")
# def delete_education(education_id: int, db: Session = Depends(get_db)):
#     education_service = EducationService(db)
#     success = education_service.delete_education(education_id)
#     if not success:
#         raise HTTPException(status_code=404, detail="Education not found")
#     return {"message": "Education deleted successfully"}
