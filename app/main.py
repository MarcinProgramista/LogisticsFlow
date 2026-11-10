from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database import get_db
from app.models.customer import Customer
from app.schemas.customer import CustomerRead
app = FastAPI()

@app.get("/health")
def health_check():
    return {
    "status": "ok",
    "application": "LogisticsFlow"
}

@app.get("/customers", response_model=list[CustomerRead])
def get_customers(db: Session = Depends(get_db)):
    statement = select(Customer)
    customers = db.scalars(statement).all()
    return customers