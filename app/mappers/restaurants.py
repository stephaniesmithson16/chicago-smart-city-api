from app.schemas.restaurants import InspectionResult


def map_inspection_row(row: dict) -> InspectionResult:
    return InspectionResult(
        name=row.get("dba_name", "Unknown"),
        address=row.get("address", "Unknown"),
        zip=row.get("zip", "Unknown"),
        risk=row.get("risk", "Unknown"),
        results=row.get("results", "Unknown"),
        inspection_date=row.get("inspection_date", "Unknown"),
        violations=row.get("violations"),
    )
