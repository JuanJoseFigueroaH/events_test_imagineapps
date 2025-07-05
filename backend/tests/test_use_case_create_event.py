from application.use_cases.create_event import CreateEventUseCase
from application.dto.event_dto import EventCreateDTO
from domain.models.event import Event
from uuid import uuid4
from datetime import datetime

class FakeEventRepo:
    def create(self, event): return event

class FakeCategoryRepo:
    def get_by_id(self, id): return True  # categoría válida

class FakeBlobService:
    def upload_image(self, file, name, type): return "https://fake.blob/image.png"

def test_create_event_use_case():
    use_case = CreateEventUseCase(FakeEventRepo(), FakeCategoryRepo(), FakeBlobService())
    dto = EventCreateDTO(
        name="Demo",
        description="Evento prueba",
        location="Medellín",
        date=datetime.now(),
        category_id=uuid4()
    )
    response = use_case.execute(dto)
    assert response.name == "Demo"
