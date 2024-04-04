# services.py
from sqlalchemy.orm import Session
from app.crud import EducationCrud
from app.model import models
from app.schema import EducationSchema


class EducationService:
    def __init__(self, db: Session):
        self.db = db

    def create_education(self, education: EducationSchema.EducationCreate):
        return EducationCrud.create_education(self.db, education)

    def get_education(self, education_id: int):
        return EducationCrud.get_education(self.db, education_id)

    def get_all_education(self, skip: int = 0, limit: int = 10):
        return EducationCrud.get_all_education(self.db, skip, limit)

    def find_education_by_organization(self, organization: str):
        return EducationCrud.find_education_by_organization(self.db, organization)

    def update_education(self, education_id: int, education_data: EducationSchema.EducationUpdate):
        return EducationCrud.update_education(self.db, education_id, education_data)

    def delete_education(self, education_id: int):
        return EducationCrud.delete_education(self.db, education_id)
