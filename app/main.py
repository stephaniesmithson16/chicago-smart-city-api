from fastapi import FastAPI

from app.api.routes import cta, health, restaurants
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(health.router, prefix=settings.app_prefix)
app.include_router(cta.router, prefix=settings.app_prefix)
app.include_router(restaurants.router, prefix=settings.app_prefix)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": f"{settings.app_name} is running"}
