from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.mappers.restaurants import map_inspection_row
from app.schemas.restaurants import InspectionResult
from app.services.ingestion import ingest_restaurant_inspections
from app.services.restaurant_data import (
    get_high_risk_restaurants,
    search_inspections,
)

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])


@router.get("/high-risk", response_model=list[InspectionResult])
def high_risk_restaurants(limit: int = 25):
    rows = get_high_risk_restaurants(limit=limit)
    return [map_inspection_row(row) for row in rows]


@router.get("/failures/recent", response_model=list[InspectionResult])
def recent_failures(limit: int = 25):
    rows = search_inspections(result="Fail", limit=limit)
    return [map_inspection_row(row) for row in rows]


@router.get("/search", response_model=list[InspectionResult])
def search(
    zip: str | None = None,
    result: str | None = Query(
        default=None, examples=["Fail", "Pass", "Pass w/ Conditions"]
    ),
    risk: str | None = None,
    limit: int = 25,
):
    rows = search_inspections(zip=zip, result=result, risk=risk, limit=limit)
    return [map_inspection_row(row) for row in rows]


@router.post("/ingest", summary="Ingest restaurant inspection data")
def ingest_inspections(
    limit: int = Query(default=100, ge=1, le=1000),
    db: Session = Depends(get_db),
) -> dict[str, int]:
    inserted = ingest_restaurant_inspections(db=db, limit=limit)
    return {"rows_inserted": inserted}
