# LogisticsFlow

<p align="center">
  <img src="docs/images/logisticsflow-banner.png"
       alt="LogisticsFlow - Transport and Logistics Management"
       width="100%">
</p>

**A logistics management REST API built with Python, FastAPI and PostgreSQL.**

## About the Project

LogisticsFlow is a backend portfolio project designed to manage transport orders and daily operations in a transport company.

The project combines practical logistics experience with backend development skills.

The main goal is to build a REST API that supports transport order management, shipment details, loading and unloading operations, route planning and resource allocation.

The application is being developed incrementally, following software engineering practices such as database migrations, data validation, automated testing and version control.

## Project Goals

- Manage transport orders (CRUD operations).
- Handle cargo information, including weight, dimensions and pallet quantities.
- Manage loading and unloading points.
- Assign vehicles and drivers to transport orders.
- Track transport order statuses and events.
- Validate incoming data.
- Implement automated tests.
- Build a maintainable backend architecture.

## Technology Stack

| Technology     | Purpose                           |
| -------------- | --------------------------------- |
| Python 3.10    | Backend programming language      |
| FastAPI        | REST API framework                |
| PostgreSQL     | Relational database               |
| SQLAlchemy 2.0 | ORM and database operations       |
| Alembic        | Database schema migrations        |
| Pydantic v2    | Data validation and serialization |
| Pytest         | Automated testing                 |
| Git            | Version control                   |

## Project Structure

```text
LogisticsFlow/
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   └── customer.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── customer.py
│   ├── __init__.py
│   ├── database.py
│   └── main.py
├── docs/
│   ├── images/
│   │   └── logisticsflow-banner.png
│   └── LogisticsFlow_baza_danych_customers_notatki.pdf
├── migrations/
│   ├── versions/
│   │   ├── 831de808085d_create_customers_table.py
│   │   └── 03e6ebd236c5_update_customer_address_fields.py
│   ├── env.py
│   ├── README
│   └── script.py.mako
├── tests/
│   ├── __init__.py
│   └── test_customer_schema.py
├── alembic.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Database

LogisticsFlow uses PostgreSQL as its relational database.

SQLAlchemy 2.0 is used to define database models and manage database operations. Alembic is responsible for tracking and applying database schema changes.

### Customer Model

The `customers` table stores customer company information and billing address details.

Implemented fields:

| Field              | Type                     | Description                      |
| ------------------ | ------------------------ | -------------------------------- |
| `id`               | Integer                  | Primary key                      |
| `company_name`     | VARCHAR(255)             | Customer company name            |
| `email`            | VARCHAR(255)             | Contact email address            |
| `phone`            | VARCHAR(20)              | Contact phone number             |
| `contact_person`   | VARCHAR(150)             | Customer contact person          |
| `street`           | VARCHAR(150)             | Billing street                   |
| `building_number`  | VARCHAR(20)              | Building number                  |
| `apartment_number` | VARCHAR(20)              | Optional apartment number        |
| `postal_code`      | VARCHAR(20)              | Postal code                      |
| `city`             | VARCHAR(100)             | City                             |
| `country`          | VARCHAR(100)             | Country                          |
| `tax_id`           | VARCHAR(30)              | Unique tax identification number |
| `created_at`       | TIMESTAMP WITH TIME ZONE | Customer creation timestamp      |

The `tax_id` field supports up to 30 characters to accommodate different national tax identification formats.

The `apartment_number` field is optional. The `tax_id` field has a unique database constraint.

### Database Migrations

Database schema changes are managed with Alembic.

Implemented migrations:

- Initial creation of the `customers` table.
- Updated customer billing address structure.
- Extended `tax_id` from `VARCHAR(10)` to `VARCHAR(30)`.
- Removed the previous `address` column and introduced separate address fields.

## Data Validation

Pydantic v2 schemas are used to validate and serialize customer data.

Implemented schemas:

- `CustomerCreate` – validates incoming customer data.
- `CustomerRead` – defines the customer response structure.
- `EmailStr` – validates email addresses.
- `ConfigDict(from_attributes=True)` – enables validation directly from SQLAlchemy model attributes.

## Testing

Pytest is used for automated tests.

Current customer schema tests cover:

- Creating a customer with valid data.
- Creating a customer without an apartment number.
- Rejecting an invalid email address.
- Rejecting customer data without a required company name.

Current test results: **4 tests passed.**

Run tests:

```bash
python -m pytest -v
```

## Development Status

**Work in Progress**

### Implemented

- Initial FastAPI application setup.
- Health check endpoint (`GET /health`).
- Interactive API documentation (Swagger UI).
- GitHub repository and project structure.
- PostgreSQL database setup.
- SQLAlchemy engine and session configuration.
- Environment variable management using `python-dotenv`.
- PostgreSQL database connection verification.
- SQLAlchemy Customer model.
- Initial Alembic migration.
- Updated customer address migration.
- Updated PostgreSQL `customers` table.
- Pydantic customer schemas.
- Email validation using `EmailStr`.
- ORM object validation using `ConfigDict(from_attributes=True)`.
- Four customer schema validation tests using Pytest.

### In Progress

- Database session dependency for FastAPI (`get_db`).
- Customer CRUD endpoints.

### Planned

- Customer management API.
- Transport order management (CRUD).
- Cargo and shipment management.
- Loading and unloading point management.
- Driver and vehicle management.
- Transport tracking and event reporting.
- Automated API tests using Pytest and HTTPX.
- Docker configuration.

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/MarcinProgramista/LogisticsFlow.git
cd LogisticsFlow
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@localhost:5432/logisticsflow
```

Replace `USER` and `PASSWORD` with your PostgreSQL credentials.

Do not commit the `.env` file to the repository.

### 5. Apply database migrations

```bash
python -m alembic upgrade head
```

### 6. Start the development server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Author

**Marcin**

Backend Developer in training.

Combining over 20 years of logistics experience with backend development.

Interested in Python, FastAPI, PostgreSQL, software architecture and logistics systems.
