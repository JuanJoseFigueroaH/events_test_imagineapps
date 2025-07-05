from typing import List, Optional
from uuid import UUID
from datetime import datetime
from sqlalchemy.orm import Session
from domain.models.event import Event
from domain.repositories.event_repository import EventRepository
from infrastructure.database.models.event_model import EventModel

class EventRepositoryImpl(EventRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, event: Event) -> Event:
        db_event = EventModel(**event.__dict__)
        self.db.add(db_event)
        self.db.commit()
        self.db.refresh(db_event)
        return Event(**db_event.__dict__)

    def get_by_id(self, id: UUID) -> Optional[Event]:
        result = self.db.query(EventModel).filter_by(id=id).first()
        return Event(**result.__dict__) if result else None

    def get_all(self, skip: int, limit: int) -> List[Event]:
        result = self.db.query(EventModel).offset(skip).limit(limit).all()
        return [Event(**e.__dict__) for e in result]

    def get_by_date(self, date: datetime) -> List[Event]:
        result = self.db.query(EventModel).filter(EventModel.date == date).all()
        return [Event(**e.__dict__) for e in result]

    def delete(self, id: UUID) -> None:
        self.db.query(EventModel).filter_by(id=id).delete()
        self.db.commit()
