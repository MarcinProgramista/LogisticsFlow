from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict, Field


class CustomerCreate(BaseModel):
    company_name: str
    email: EmailStr | None = None
    phone: str | None = None
    contact_person: str
    street: str
    building_number: str
    apartment_number: str | None = None
    postal_code: str
    city: str
    country: str
    payment_terms: int = Field(default=30, gt=0)
    tax_id: str


class CustomerRead(BaseModel):
    id: int
    company_name: str
    email: EmailStr | None
    phone: str | None
    contact_person: str
    street: str
    building_number: str
    apartment_number: str | None = None
    postal_code: str
    city: str
    country: str
    tax_id: str
    payment_terms: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


