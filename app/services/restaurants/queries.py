from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.restaurant import RestaurantInspection


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
