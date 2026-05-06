from fastapi import APIRouter

from app.mappers.cta import map_cta_stations, map_train_arrival
from app.schemas.cta import CTAStation, TrainArrival
from app.services.cta_data import get_cta_stations, get_train_arrivals

router = APIRouter(prefix="/cta", tags=["CTA"])


@router.get(
    path="/stations",
    response_model=list[CTAStation],
    summary="Get CTA Stations",
)
def cta_stations() -> list[CTAStation]:
    rows = get_cta_stations()
    stations_by_map_id: dict[str, CTAStation] = {}

    for row in rows:
        station = map_cta_stations(row)
        stations_by_map_id[station.map_id] = station

    return list(stations_by_map_id.values())


@router.get(
    path="/train-arrivals",
    response_model=list[TrainArrival],
    summary="Get Train Arrivals",
)
def train_arrivals(map_id: str, limit: int = 25) -> list[TrainArrival]:
    rows = get_train_arrivals(map_id=map_id, limit=limit)

    return [map_train_arrival(row) for row in rows]
