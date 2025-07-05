from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from domain.models.category import Category

class CategoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Category]:
        pass

    @abstractmethod
    def get_by_id(self, id: UUID) -> Optional[Category]:
        pass
