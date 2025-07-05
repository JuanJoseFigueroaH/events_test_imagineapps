from application.dto.event_dto import EventCreateDTO
from domain.models.event import Event
from uuid import uuid4
from datetime import datetime

def test_event_dto_to_domain():
    dto = EventCreateDTO(
        name="Concierto",
        description="Concierto de rock",
        location="Bogotá",
        date=datetime(2025, 10, 1, 18, 0),
        category_id=uuid4()
    )

    assert dto.name == "Concierto"
    assert isinstance(dto.date, datetime)
