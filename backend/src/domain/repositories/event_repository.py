from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from datetime import datetime
from domain.models.event import Event

class EventRepository(ABC):
    @abstractmethod
    def create(self, event: Event) -> Event:
        pass

    @abstractmethod
    def get_by_id(self, id: UUID) -> Optional[Event]:
        pass

    @abstractmethod
    def get_all(self, skip: int, limit: int) -> List[Event]:
        pass

    @abstractmethod
    def get_by_date(self, date: datetime) -> List[Event]:
        pass

    @abstractmethod
    def delete(self, id: UUID) -> None:
        pass
