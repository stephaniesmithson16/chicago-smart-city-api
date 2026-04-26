from fastapi import FastAPI

from app.api.routes import cta, health, restaurants
from app.core.config import settings

app = FastAPI(
    title=settings.api_name,
    version=settings.api_version,
)

app.include_router(health.router, prefix=settings.api_prefix)
app.include_router(cta.router, prefix=settings.api_prefix)
app.include_router(restaurants.router, prefix=settings.api_prefix)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": f"{settings.api_name} is running"}
