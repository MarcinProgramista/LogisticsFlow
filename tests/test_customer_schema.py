import pytest
from pydantic import ValidationError
from app.schemas.customer import CustomerCreate

def test_customer_create_valid_data():
    customer = CustomerCreate(
        company_name="ABC Transport",
        email="biuro@abc.pl",
        phone="123456789",
        contact_person="Jan Kowalski",
        street="Kilińskiego",
        building_number="5",
        apartment_number="10",
        postal_code="22-400",
        city="Zamość",
        country="PL",
        payment_terms="45",
        tax_id="1234567890"
    )
    assert customer.company_name == "ABC Transport"
    assert customer.email == "biuro@abc.pl"

def test_customer_create_without_apartament_number():
    customer = CustomerCreate(
        company_name="ABC Transport",
        email="biuro@abc.pl",
        phone="123456789",
        contact_person="Jan Kowalski",
        street="Kilińskiego",
        building_number="5",
        postal_code="22-400",
        city="Zamość",
        country="PL",
        payment_terms="45",
        tax_id="1234567890"
    )
    assert customer.apartment_number is None 

def test_customer_create_invalid_email():
    with pytest.raises(ValidationError):
        CustomerCreate(
            company_name="ABC Transport",
            email="biuro-abc.pl",
            phone="123456789",
            contact_person="Jan Kowalski",
            street="Kilińskiego",
            building_number="5",
            postal_code="22-400",
            city="Zamość",
            country="PL",
            payment_terms="45",
            tax_id="1234567890"
        )

def test_customer_create_missing_company_name():
    with pytest.raises(ValidationError):
       CustomerCreate(
           email="biuro@abc.pl",
           phone="123456789",
           contact_person="Jan Kowalski",
           street="Kilińskiego",
           building_number="5",
           postal_code="22-400",
           city="Zamość",
           country="PL",
           payment_terms="45",
           tax_id="1234567890"
       )
def test_customer_create_without_email():
   
    customer = CustomerCreate(
            company_name="ABC Transport",
           phone="123456789",
           contact_person="Jan Kowalski",
           street="Kilińskiego",
           building_number="5",
           postal_code="22-400",
           city="Zamość",
           country="PL",
           payment_terms="45",
           tax_id="1234567890" 
           )
    assert customer.email is None   
    