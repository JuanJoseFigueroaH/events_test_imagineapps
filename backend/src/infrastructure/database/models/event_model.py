from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from infrastructure.database.db import Base

class EventModel(Base):
    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    location = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    image_url = Column(String, nullable=True)

    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"), nullable=False)
    category = relationship("CategoryModel", back_populates="events")
