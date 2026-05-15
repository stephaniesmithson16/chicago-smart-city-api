from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.services.restaurants.ingestion import backfill_inspections

router = APIRouter(prefix="/restaurants/ingest", tags=["Restaurant Ingestion"])


@router.post(
    "/ingest_batch", summary="Ingest restaurant inspection data in batches"
)
def ingest_inspections_batch(
    start_date: str,
    end_date: str,
    batch_size: int = Query(default=500, ge=1, le=1000),
    max_batches: int = Query(default=5, ge=1, le=10),
    db: Session = Depends(get_db),
) -> dict[str, int]:
    return backfill_inspections(
        db=db,
        start_date=start_date,
        end_date=end_date,
        batch_size=batch_size,
        max_batches=max_batches,
    )
