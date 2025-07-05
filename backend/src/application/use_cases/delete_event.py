from uuid import UUID
from domain.repositories.event_repository import EventRepository

class DeleteEventUseCase:
    def __init__(self, event_repo: EventRepository):
        self.event_repo = event_repo

    def execute(self, id: UUID) -> None:
        event = self.event_repo.get_by_id(id)
        if not event:
            raise ValueError("Evento no encontrado")
        self.event_repo.delete(id)
