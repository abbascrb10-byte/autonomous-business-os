from fastapi import FastAPI
from app.config.settings import settings
from app.database.session import init_db
from app.api.routes import router as api_router
from app.api.health import router as health_router
from app.api.admin import router as admin_router

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
def startup():
    init_db()

app.include_router(health_router, prefix="/api")
app.include_router(api_router, prefix="/api")
app.include_router(admin_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to Global Purchase Intent Engine (GPIE)"}
