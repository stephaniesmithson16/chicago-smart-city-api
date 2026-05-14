import httpx

from app.core.config import settings

FOOD_INSPECTIONS_URL = settings.food_inspections_url


def get_high_risk_restaurants(limit: int = 10) -> list[dict]:
    params = {
        "$limit": limit,
        "$where": "risk = 'Risk 1 (High)'",
        "$order": "inspection_date DESC",
    }

    response = httpx.get(FOOD_INSPECTIONS_URL, params=params, timeout=10.0)
    response.raise_for_status()

    return response.json()


def search_inspections(
    zip: str | None = None,
    result: str | None = None,
    risk: str | None = None,
    limit: int = 25,
) -> list[dict]:
    filters = []

    if zip:
        filters.append(f"zip = '{zip}'")

    if result:
        filters.append(f"results = '{result}'")

    if risk:
        filters.append(f"risk = '{risk}'")

    params = {
        "$limit": limit,
        "$order": "inspection_date DESC",
    }

    if filters:
        params["$where"] = " AND ".join(filters)

    response = httpx.get(FOOD_INSPECTIONS_URL, params=params, timeout=10.0)
    response.raise_for_status()

    return response.json()
