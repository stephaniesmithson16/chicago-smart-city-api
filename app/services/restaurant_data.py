import httpx
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models.restaurant import RestaurantInspection

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


def search_db_inspections(
    db: Session,
    zip: str | None = None,
    result: str | None = None,
    risk: str | None = None,
    limit: int = 100,
) -> list[RestaurantInspection]:
    filters = []

    if zip:
        filters.append(RestaurantInspection.zip_code == zip)
    if result:
        filters.append(RestaurantInspection.results == result)
    if risk:
        filters.append(RestaurantInspection.risk == risk)

    stmt = (
        select(RestaurantInspection)
        .where(*filters)
        .order_by(RestaurantInspection.inspection_date.desc())
        .limit(limit)
    )

    return list(db.scalars(stmt).all())
