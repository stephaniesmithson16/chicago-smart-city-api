from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.mappers.restaurants import map_inspection_model
from app.schemas.restaurants import InspectionResult
from app.services.restaurants.queries import search_db_inspections

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])


@router.get("/inspections", response_model=list[InspectionResult])
def search_db(
    zip_code: str | None = None,
    result: str | None = None,
    risk: str | None = None,
    limit: int = Query(default=25, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    sort_by: str = Query(default="inspection_date"),
    sort_order: str = Query(default="desc"),
    db: Session = Depends(get_db),
):
    rows = search_db_inspections(
        db=db,
        zip_code=zip_code,
        result=result,
        risk=risk,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_order=sort_order,
    )
    return [map_inspection_model(row) for row in rows]
