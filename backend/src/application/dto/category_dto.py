from pydantic import BaseModel
from uuid import UUID

class CategoryResponseDTO(BaseModel):
    id: UUID
    name: str
