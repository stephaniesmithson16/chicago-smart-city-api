from app.schemas.restaurants import InspectionResult


def map_inspection_row(row: dict) -> InspectionResult:
    return InspectionResult(
        inspection_id=row.get("inspection_id", 0),
        name=row.get("dba_name", "Unknown"),
        aka_name=row.get("aka_name", "Unknown"),
        license=row.get("license_", "Unknown"),
        facility_type=row.get("facility_type", "Unknown"),
        address=row.get("address", "Unknown"),
        zip=row.get("zip", "Unknown"),
        risk=row.get("risk", "Unknown"),
        results=row.get("results", "Unknown"),
        inspection_date=row.get("inspection_date", "Unknown"),
        inspection_type=row.get("inspection_type", "Unknown"),
        violations=row.get("violations"),
    )
