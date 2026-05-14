from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app.db.models.restaurant import RestaurantInspection
from app.services.restaurants.chicago_client import search_inspections


def ingest_restaurant_inspections(db: Session, limit: int = 100) -> int:
    rows = search_inspections(limit=limit)

    inserted = 0

    for row in rows:
        statement = (
            insert(RestaurantInspection)
            .values(
                inspection_id=row.get("inspection_id"),
                name=row.get("dba_name"),
                aka_name=row.get("aka_name"),
                license=row.get("license_"),
                facility_type=row.get("facility_type"),
                address=row.get("address"),
                zip_code=row.get("zip"),
                risk=row.get("risk"),
                results=row.get("results"),
                inspection_date=row.get("inspection_date", "")[:10],
                inspection_type=row.get("inspection_type"),
                violations=row.get("violations"),
            )
            .on_conflict_do_nothing(index_elements=["inspection_id"])
            .returning(RestaurantInspection.id)
        )

        inserted_id = db.execute(statement).scalar_one_or_none()
        if inserted_id is not None:
            inserted += 1

    db.commit()
    return inserted
