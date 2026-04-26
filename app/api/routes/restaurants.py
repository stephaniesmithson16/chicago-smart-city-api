from fastapi import APIRouter

from app.schemas.restaurants import InspectionResult
from app.services.chicago_data import get_high_risk_restaurants

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
        )
        for row in rows
    ]
