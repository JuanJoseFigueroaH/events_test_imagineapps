from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID
from typing import Optional

class EventCreateDTO(BaseModel):
    name: str
    description: str
    location: str
    date: datetime
    category_id: UUID

class EventResponseDTO(BaseModel):
    id: UUID
    name: str
    description: str
    location: str
    date: datetime
    category_id: UUID
    image_url: Optional[str]
