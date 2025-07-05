from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from domain.models.category import Category
from domain.repositories.category_repository import CategoryRepository
from infrastructure.database.models.category_model import CategoryModel

class CategoryRepositoryImpl(CategoryRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Category]:
        result = self.db.query(CategoryModel).all()
        return [Category(**c.__dict__) for c in result]

    def get_by_id(self, id: UUID) -> Optional[Category]:
        result = self.db.query(CategoryModel).filter_by(id=id).first()
        return Category(**result.__dict__) if result else None
