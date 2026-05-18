from app.db.models.restaurant import RestaurantInspection
from app.schemas.restaurants import InspectionResult


def map_inspection_row(row: dict) -> InspectionResult:
    return InspectionResult(
        inspection_id=row.get("inspection_id", 0),
        name=row.get("dba_name", "Unknown"),
        aka_name=row.get("aka_name", "Unknown"),
        license=row.get("license_", "Unknown"),
        facility_type=row.get("facility_type", "Unknown"),
        address=row.get("address", "Unknown"),
        zip_code=row.get("zip", "Unknown"),
        risk=row.get("risk", "Unknown"),
        results=row.get("results", "Unknown"),
        inspection_date=row.get("inspection_date", "Unknown"),
        inspection_type=row.get("inspection_type", "Unknown"),
        violations=row.get("violations"),
    )


def map_inspection_model(row: RestaurantInspection) -> InspectionResult:
    return InspectionResult(
        inspection_id=row.inspection_id,
        name=row.name,
        aka_name=row.aka_name,
        license=row.license,
        facility_type=row.facility_type,
        address=row.address,
        zip_code=row.zip_code,
        risk=row.risk,
        results=row.results,
        inspection_date=row.inspection_date,
        inspection_type=row.inspection_type,
        violations=row.violations,
    )
