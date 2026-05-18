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
    zip_code: str | None = None,
    result: str | None = None,
    risk: str | None = None,
    limit: int = 25,
) -> list[dict]:
    filters = []

    if zip_code:
        filters.append(f"zip = '{zip_code}'")

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


def load_inspections(
    start_date: str | None = None,
    end_date: str | None = None,
    offset: int = 0,
    limit: int = 100,
) -> list[dict]:
    params = {
        "$limit": limit,
        "$offset": offset,
        "$order": "inspection_date DESC",
    }

    filters = []

    if start_date:
        filters.append(f"inspection_date >= '{start_date}'")

    if end_date:
        filters.append(f"inspection_date <= '{end_date}'")

    if filters:
        params["$where"] = " AND ".join(filters)

    response = httpx.get(
        FOOD_INSPECTIONS_URL,
        params=params,
        timeout=15.0,
    )
    response.raise_for_status()

    return response.json()
