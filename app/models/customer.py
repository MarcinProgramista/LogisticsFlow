from datetime import datetime, timezone

from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    company_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )
    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )
    contact_person: Mapped[str] = mapped_column(String(150), nullable=False)
    street: Mapped[str] = mapped_column(String(150), nullable=False)
    building_number: Mapped[str] = mapped_column(String(20), nullable=False)
    apartment_number: Mapped[str] = mapped_column(String(20), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    tax_id: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    payment_terms: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=30
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )