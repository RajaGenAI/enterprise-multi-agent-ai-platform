from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Multi-Agent AI Platform",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {
        "message": "Enterprise Multi-Agent AI Platform is running"
    }