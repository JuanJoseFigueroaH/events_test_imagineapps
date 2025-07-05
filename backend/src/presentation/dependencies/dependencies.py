from fastapi import Depends
from sqlalchemy.orm import Session
from infrastructure.database.db import SessionLocal
from infrastructure.repositories.event_repository_impl import EventRepositoryImpl
from infrastructure.repositories.category_repository_impl import CategoryRepositoryImpl
from infrastructure.services.azure_blob_service import AzureBlobService
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from fastapi import HTTPException, status
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_event_repo(db: Session = Depends(get_db)):
    return EventRepositoryImpl(db)

def get_category_repo(db: Session = Depends(get_db)):
    return CategoryRepositoryImpl(db)

def get_blob_service():
    return AzureBlobService()

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = "HS256"

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
