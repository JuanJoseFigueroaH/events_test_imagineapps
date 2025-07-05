from datetime import datetime
from typing import List
from domain.repositories.event_repository import EventRepository
from application.dto.event_dto import EventResponseDTO

class FilterEventsByDateUseCase:
    def __init__(self, event_repo: EventRepository):
        self.event_repo = event_repo

    def execute(self, date: datetime) -> List[EventResponseDTO]:
        events = self.event_repo.get_by_date(date)
        return [EventResponseDTO(**e.__dict__) for e in events]
