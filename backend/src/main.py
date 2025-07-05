from fastapi import FastAPI
from presentation.routers.event_router import router as event_router
from infrastructure.database.db import Base, engine
from presentation.routers.auth_router import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gestión de Eventos", version="1.0")

app.include_router(event_router)
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de eventos"}
