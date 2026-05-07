from sqlalchemy.orm import Session

from app.db.models.restaurant import RestaurantInspection
from app.services.restaurant_data import search_inspections


def ingest_restaurant_inspections(db: Session, limit: int = 100) -> int:
    rows = search_inspections(limit=limit)

    inserted = 0

    for row in rows:
        inspection = RestaurantInspection(
            name=row.get("dba_name"),
            address=row.get("address"),
            zip_code=row.get("zip"),
            inspection_date=row.get("inspection_date", "")[:10],
            results=row.get("results"),
            risk=row.get("risk"),
            violations=row.get("violations"),
        )

        db.add(inspection)
        inserted += 1

    db.commit()
    return inserted
