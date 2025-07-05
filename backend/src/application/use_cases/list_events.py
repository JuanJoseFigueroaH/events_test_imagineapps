from typing import List
from domain.repositories.event_repository import EventRepository
from application.dto.event_dto import EventResponseDTO

class ListEventsUseCase:
    def __init__(self, event_repo: EventRepository):
        self.event_repo = event_repo

    def execute(self, skip: int = 0, limit: int = 10) -> List[EventResponseDTO]:
        events = self.event_repo.get_all(skip, limit)
        return [EventResponseDTO(**e.__dict__) for e in events]
