from fastapi import APIRouter, Query

from app.mappers.restaurants import map_inspection_row
from app.schemas.restaurants import InspectionResult
from app.services.restaurant_data import get_high_risk_restaurants, search_inspections

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
    result: str | None = Query(default=None, examples=["Fail", "Pass", "Pass w/ Conditions"]),
    risk: str | None = None,
    limit: int = 25,
):
    rows = search_inspections(zip=zip, result=result, risk=risk, limit=limit)
    return [map_inspection_row(row) for row in rows]
