from datetime import datetime
from uuid import UUID
from typing import Optional

class Event:
    def __init__(
        self,
        id: UUID,
        name: str,
        description: str,
        location: str,
        date: datetime,
        category_id: UUID,
        image_url: Optional[str] = None
    ):
        self.id = id
        self.name = name
        self.description = description
        self.location = location
        self.date = date
        self.category_id = category_id
        self.image_url = image_url
