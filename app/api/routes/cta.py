from fastapi import APIRouter

from app.schemas.cta import CTAStation

router = APIRouter(prefix="/cta", tags=["CTA"])


@router.get(path="/stations", response_model=list[CTAStation], summary="Get CTA Stations")
def get_cta_stations() -> list[CTAStation]:
    return [
        CTAStation(
            station_id=1,
            name="Logan Square",
            line="Blue",
            neighborhood="Logan Square",
        ),
        CTAStation(
            station_id=2,
            name="Southport",
            line="Brown",
            neighborhood="Lakeview",
        ),
        CTAStation(
            station_id=3,
            name="Chicago",
            line="Red",
            neighborhood="River North",
        ),
    ]
