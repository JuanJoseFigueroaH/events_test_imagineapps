from fastapi import APIRouter, Depends, UploadFile, File, Form, Query
from application.use_cases.create_event import CreateEventUseCase
from application.use_cases.list_events import ListEventsUseCase
from application.use_cases.filter_events_by_date import FilterEventsByDateUseCase
from application.use_cases.delete_event import DeleteEventUseCase
from application.dto.event_dto import EventCreateDTO, EventResponseDTO
from presentation.dependencies.dependencies import (
    get_event_repo, get_category_repo, get_blob_service, get_current_user
)
from domain.repositories.event_repository import EventRepository
from domain.repositories.category_repository import CategoryRepository
from infrastructure.services.azure_blob_service import AzureBlobService
from uuid import UUID
from datetime import datetime
from typing import List

router = APIRouter(prefix="/events", tags=["Eventos"])

@router.post("/", response_model=EventResponseDTO)
async def create_event(
    name: str = Form(...),
    description: str = Form(...),
    location: str = Form(...),
    date: datetime = Form(...),
    category_id: UUID = Form(...),
    image: UploadFile = File(None),
    event_repo: EventRepository = Depends(get_event_repo),
    category_repo: CategoryRepository = Depends(get_category_repo),
    blob_service: AzureBlobService = Depends(get_blob_service),
    user: dict = Depends(get_current_user)
):
    file_bytes = await image.read() if image else None
    content_type = image.content_type if image else ""
    dto = EventCreateDTO(name=name, description=description, location=location, date=date, category_id=category_id)
    use_case = CreateEventUseCase(event_repo, category_repo, blob_service)
    return use_case.execute(dto, file_bytes, image.filename if image else "", content_type)

@router.get("/", response_model=List[EventResponseDTO])
def list_events(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    event_repo: EventRepository = Depends(get_event_repo),
    user: dict = Depends(get_current_user)
):
    use_case = ListEventsUseCase(event_repo)
    return use_case.execute(skip, limit)

@router.get("/by-date", response_model=List[EventResponseDTO])
def filter_by_date(
    date: datetime = Query(...),
    event_repo: EventRepository = Depends(get_event_repo),
    user: dict = Depends(get_current_user)
):
    use_case = FilterEventsByDateUseCase(event_repo)
    return use_case.execute(date)

@router.delete("/{event_id}", status_code=204)
def delete_event(
    event_id: UUID,
    event_repo: EventRepository = Depends(get_event_repo),
    user: dict = Depends(get_current_user)
):
    use_case = DeleteEventUseCase(event_repo)
    use_case.execute(event_id)
    return
