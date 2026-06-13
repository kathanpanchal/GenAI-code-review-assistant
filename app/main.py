from fastapi import FastAPI

from app.github.webhook import router as webhook_router
from app.cache.cache_metrics import CacheMetrics

app = FastAPI()

app.include_router(webhook_router)

@app.get("/")
def health_check():
    return {"status": "running"}

@app.get("/metrics")
def get_metrics():
    return CacheMetrics.get_stats()