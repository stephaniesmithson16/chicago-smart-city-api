from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.services.restaurants.ingestion import backfill_inspections

router = APIRouter(prefix="/admin/restaurants", tags=["Admin - Restaurants"])


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


@router.post(
    "/ingest/sync",
    summary="Sync restaurant inspection data from the source API",
)
def sync_inspections(
    lookback_days: int = Query(default=30, ge=1, le=365),
    batch_size: int = Query(default=500, ge=1, le=1000),
    max_batches: int = Query(default=5, ge=1, le=10),
    db: Session = Depends(get_db),
) -> dict[str, int]:
    end_date = datetime.today()
    start_date = end_date - timedelta(days=lookback_days)

    return backfill_inspections(
        db=db,
        start_date=start_date.strftime("%Y-%m-%d"),
        end_date=end_date.strftime("%Y-%m-%d"),
        batch_size=batch_size,
        max_batches=max_batches,
    )
