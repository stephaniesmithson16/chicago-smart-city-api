from sqlalchemy import Column, Integer, String, Text

from app.db.base import Base


class RestaurantInspection(Base):
    __tablename__ = "restaurant_inspections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    zip_code = Column(String)
    risk = Column(String)
    results = Column(String)
    inspection_date = Column(String)
    violations = Column(Text)
