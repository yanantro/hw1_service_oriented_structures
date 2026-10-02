import os
from datetime import datetime, timezone
from fastapi import FastAPI

SERVICE_NAME = os.getenv("SERVICE_NAME", "catalog-service")
SERVICE_VERSION = os.getenv("SERVICE_VERSION", "0.1.0")

app = FastAPI(
    title="Marketplace Catalog Service",
    version=SERVICE_VERSION,
    description="Каркас сервиса каталога товаров",
)


@app.get("/health", tags=["service"])
def health() -> dict:
    return {
        "status": "ok",
        "service": SERVICE_NAME,
        "version": SERVICE_VERSION,
        "time": datetime.now(timezone.utc).isoformat(),
    }

@app.get("/", tags=["service"])
def root() -> dict:
    return {"service": SERVICE_NAME, "docs": "/docs", "health": "/health"}
