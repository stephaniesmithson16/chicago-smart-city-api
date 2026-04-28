import httpx
from fastapi import HTTPException

from app.core.config import settings


def get_cta_stations() -> list[dict]:
    response = httpx.get(settings.cta_stations_url, timeout=10.0)
    response.raise_for_status()
    return response.json()


def get_train_arrivals(map_id: str, limit: int = 10) -> list[dict]:
    if not settings.cta_train_tracker_api_key:
        raise HTTPException(status_code=500, detail="CTA Train Tracker API key is not configured.")

    params = {
        "key": settings.cta_train_tracker_api_key,
        "mapid": map_id,
        "max": limit,
        "outputType": "JSON",
    }

    response = httpx.get(settings.cta_train_arrivals_url, params=params, timeout=10.0)
    response.raise_for_status()

    data = response.json()
    return data.get("ctatt", {}).get("eta", [])
