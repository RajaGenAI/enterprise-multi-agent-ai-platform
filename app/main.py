from fastapi import FastAPI
from app.api.v1.health import router as health_router

app = FastAPI(
    title="Enterprise Multi-Agent AI Platform",
    version="0.1.0",
)

# Direct inclusion for testing
app.include_router(health_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Enterprise Multi-Agent AI Platform is running"}