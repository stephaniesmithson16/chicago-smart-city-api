from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.api.routes import (
    cta,
    health,
    restaurant_ingestion,
    restaurant_source,
    restaurants,
)
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(health.router, prefix=settings.app_prefix)
app.include_router(cta.router, prefix=settings.app_prefix)
app.include_router(restaurants.router, prefix=settings.app_prefix)
app.include_router(restaurant_ingestion.router, prefix=settings.app_prefix)
app.include_router(restaurant_source.router, prefix=settings.app_prefix)


@app.get("/")
def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")
