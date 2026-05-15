from sqlalchemy import asc, desc, select
from sqlalchemy.orm import Session

from app.db.models.restaurant import RestaurantInspection

ALLOWED_SORT_FIELDS = {
    "inspection_date": RestaurantInspection.inspection_date,
    "name": RestaurantInspection.name,
    "results": RestaurantInspection.results,
    "risk": RestaurantInspection.risk,
    "zip_code": RestaurantInspection.zip_code,
}


def search_db_inspections(
    db: Session,
    zip: str | None = None,
    result: str | None = None,
    risk: str | None = None,
    offset: int = 0,
    sort_by: str = "inspection_date",
    sort_order: str = "desc",
    limit: int = 100,
) -> list[RestaurantInspection]:
    statement = select(RestaurantInspection)

    if zip:
        statement = statement.where(RestaurantInspection.zip_code == zip)

    if result:
        statement = statement.where(RestaurantInspection.results == result)

    if risk:
        statement = statement.where(RestaurantInspection.risk == risk)

    sort_column = ALLOWED_SORT_FIELDS.get(
        sort_by, RestaurantInspection.inspection_date
    )

    if sort_order == "asc":
        statement = statement.order_by(asc(sort_column))
    else:
        statement = statement.order_by(desc(sort_column))

    statement = statement.limit(limit).offset(offset)

    return list(db.scalars(statement).all())
