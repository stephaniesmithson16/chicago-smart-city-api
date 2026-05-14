from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class RestaurantInspection(Base):
    __tablename__ = "restaurant_inspections"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    inspection_id: Mapped[int] = mapped_column(
        Integer, nullable=False, unique=True
    )

    name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    aka_name: Mapped[str | None] = mapped_column(String, nullable=True)
    license: Mapped[str | None] = mapped_column(String, nullable=True)
    facility_type: Mapped[str | None] = mapped_column(String, nullable=True)
    address: Mapped[str | None] = mapped_column(String, nullable=True)
    zip_code: Mapped[str | None] = mapped_column(String, nullable=True)
    risk: Mapped[str | None] = mapped_column(String, nullable=True)
    results: Mapped[str | None] = mapped_column(String, nullable=True)
    inspection_date: Mapped[str | None] = mapped_column(String, nullable=True)
    inspection_type: Mapped[str | None] = mapped_column(String, nullable=True)
    violations: Mapped[str | None] = mapped_column(Text, nullable=True)
