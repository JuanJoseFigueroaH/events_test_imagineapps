from domain.models.event import Event
from domain.repositories.event_repository import EventRepository
from domain.repositories.category_repository import CategoryRepository
from application.dto.event_dto import EventCreateDTO, EventResponseDTO
from infrastructure.services.azure_blob_service import AzureBlobService
from uuid import uuid4

class CreateEventUseCase:
    def __init__(
        self,
        event_repo: EventRepository,
        category_repo: CategoryRepository,
        blob_service: AzureBlobService
    ):
        self.event_repo = event_repo
        self.category_repo = category_repo
        self.blob_service = blob_service

    def execute(self, data: EventCreateDTO, image: bytes = None, filename: str = "", content_type: str = "") -> EventResponseDTO:
        category = self.category_repo.get_by_id(data.category_id)
        if not category:
            raise ValueError("Categoría no encontrada")

        image_url = None
        if image:
            image_url = self.blob_service.upload_image(image, filename, content_type)

        new_event = Event(
            id=uuid4(),
            name=data.name,
            description=data.description,
            location=data.location,
            date=data.date,
            category_id=data.category_id,
            image_url=image_url
        )

        created = self.event_repo.create(new_event)
        return EventResponseDTO(**created.__dict__)
