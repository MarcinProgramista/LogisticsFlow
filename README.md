# LogisticsFlow

<p align="center">
  <img src="docs/images/logisticsflow-banner.png"
       alt="LogisticsFlow - Transport and Logistics Management"
       width="100%">
</p>

**A logistics management API built with Python, FastAPI and PostgreSQL.**

## About the Project

LogisticsFlow is a backend portfolio project designed to manage transport orders and daily operations in a transport company.

The project combines practical logistics knowledge with backend development skills.

The main goal is to build a REST API that supports transport order management, shipment details, route planning and resource allocation.

## Project Goals

- Manage transport orders (CRUD operations).
- Handle cargo information, including weight, dimensions and pallet quantities.
- Manage loading and unloading points.
- Assign vehicles and drivers to transport orders.
- Track order statuses and transport events.
- Validate incoming data.
- Implement automated tests.

## Technology Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Pytest
- Git

## Project Structure

```text
LogisticsFlow/
├── app/
│   ├── __init__.py
│   └── main.py
├── docs/
│   └── images/
│       └── logisticsflow-banner.png
├── requirements.txt
├── .gitignore
└── README.md
```

## Development Status

**Work in Progress**

### Implemented
- Initial FastAPI application setup.
- Health check endpoint (`GET /health`).
- Interactive API documentation (Swagger UI).
- GitHub repository and project structure.

### In Progress
- Business requirements analysis.
- Transport order data model design.
- Database architecture planning.

### Planned
- PostgreSQL integration.
- SQLAlchemy ORM and Alembic migrations.
- Customer management.
- Transport order management (CRUD).
- Cargo and route management.
- Drivers and vehicles management.
- Transport tracking and event reporting.
- Automated tests with pytest.

## Author

Marcin – Backend Developer in training.

Interested in Python, backend development, databases and logistics systems.
