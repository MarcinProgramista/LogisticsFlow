import os
import pytest

from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db
from app.models.customer import Customer

load_dotenv()

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

test_engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine
)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client():
    Base.metadata.create_all(bind=test_engine)
    app.dependency_overrides[get_db] = override_get_db

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        Base.metadata.drop_all(bind=test_engine)
        app.dependency_overrides.clear()

def test_get_customers_empty(client):
    response = client.get("/customers")

    assert response.status_code == 200
    assert response.json() == []

def test_get_customers_returns_customer(client):
    customer = Customer(
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
        payment_terms=45,
        tax_id="1234567890"
    )
    db = TestingSessionLocal()
    try:
        db.add(customer)
        db.commit()
    finally:
        db.close()
        
    response = client.get("/customers")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["company_name"] == "ABC Transport"
    assert response.json()[0]["payment_terms"] == 45
