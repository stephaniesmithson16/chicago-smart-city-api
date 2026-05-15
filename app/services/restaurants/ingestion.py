from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app.db.models.restaurant import RestaurantInspection
from app.services.restaurants.chicago_client import (
    load_inspections,
)


def insert_restaurant_inspections(db: Session, rows: list[dict]) -> int:
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


def backfill_inspections(
    db: Session,
    start_date: str,
    end_date: str,
    batch_size: int = 500,
    max_batches: int = 5,
) -> dict[str, int]:
    total_seen = 0
    total_inserted = 0
    offset = 0

    for _ in range(max_batches):
        rows = load_inspections(
            limit=batch_size,
            offset=offset,
            start_date=start_date,
            end_date=end_date,
        )

        if not rows:
            break

        inserted = insert_restaurant_inspections(db=db, rows=rows)

        total_seen += len(rows)
        total_inserted += inserted

        if len(rows) < batch_size:
            break

        offset += batch_size

    return {
        "records_seen": total_seen,
        "records_inserted": total_inserted,
    }
