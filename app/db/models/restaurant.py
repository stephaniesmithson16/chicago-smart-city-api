from sqlalchemy import Column, Integer, String, Text

from app.db.base import Base


class RestaurantInspection(Base):
    __tablename__ = "restaurant_inspections"

    id = Column(Integer, primary_key=True, index=True)

    inspection_id = Column(Integer, nullable=False, unique=True)

    name = Column(String, index=True, nullable=False)
    aka_name = Column(String, nullable=True)
    license = Column(String, nullable=True)
    facility_type = Column(String, nullable=True)
    address = Column(String, nullable=True)
    zip_code = Column(String, nullable=True)
    risk = Column(String, nullable=True)
    results = Column(String, nullable=True)
    inspection_date = Column(String, nullable=True)
    inspection_type = Column(String, nullable=True)
    violations = Column(Text, nullable=True)
