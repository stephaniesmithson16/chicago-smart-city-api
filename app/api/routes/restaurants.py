from fastapi import APIRouter, Query

from app.schemas.restaurants import InspectionResult
from app.services.chicago_data import get_high_risk_restaurants, search_inspections

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])


@router.get("/high-risk", response_model=list[InspectionResult])
def high_risk_restaurants():
    rows = get_high_risk_restaurants()

    return [
        InspectionResult(
            name=row.get("dba_name", "Unknown"),
            address=row.get("address", "Unknown"),
            risk=row.get("risk", "Unknown"),
            results=row.get("results", "Unknown"),
            inspection_date=row.get("inspection_date", "")[:10],
            violations=row.get("violations", "None"),
        )
        for row in rows
    ]


@router.get("/search", response_model=list[InspectionResult])
def search(
    zip: str | None = None,
    result: str | None = Query(default=None, examples=["Fail", "Pass", "Pass w/ Conditions"]),
    risk: str | None = None,
    limit: int = 25,
):
    rows = search_inspections(zip=zip, result=result, risk=risk, limit=limit)

    return [
        InspectionResult(
            name=row.get("dba_name", "Unknown"),
            address=row.get("address", "Unknown"),
            risk=row.get("risk", "Unknown"),
            results=row.get("results", "Unknown"),
            inspection_date=row.get("inspection_date", "")[:10],
            violations=row.get("violations", "None"),
        )
        for row in rows
    ]
