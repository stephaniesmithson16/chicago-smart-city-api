from fastapi import APIRouter

from app.core.config import get_settings
from app.schemas.health import HealthCheck

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthCheck)
def health_check() -> HealthCheck:
    settings = get_settings()
    return HealthCheck(status="ok", app=settings.app_name, environment=settings.environment)
