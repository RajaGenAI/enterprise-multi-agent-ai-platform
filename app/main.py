from fastapi import FastAPI
from app.api.v1.health import router as health_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

# Direct inclusion for testing
app.include_router(health_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Enterprise Multi-Agent AI Platform is running"}