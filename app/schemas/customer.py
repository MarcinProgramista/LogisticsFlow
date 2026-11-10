from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict


class CustomerCreate(BaseModel):
    company_name: str
    email: EmailStr
    phone: str
    contact_person: str
    address: str
    tax_id: str


class CustomerRead(BaseModel):
    id: int
    company_name: str
    email: EmailStr
    phone: str
    contact_person: str
    address: str
    tax_id: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

