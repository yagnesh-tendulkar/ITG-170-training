# TODO App

A production-ready TODO application built with FastAPI and SQLAlchemy.

## Project Overview

This is a comprehensive TODO management application that demonstrates modern Python web development practices, including RESTful API design, database management, and dependency injection patterns.

## Project Structure
TODO/ ├── app/ │ ├── database/ │ │ └── connection.py # Database configuration and session management │ ├── models/ # SQLAlchemy ORM models │ ├── routes/ # API endpoint definitions │ ├── schemas/ # Pydantic data models for validation │ └── main.py # FastAPI application entry point ├── requirements.txt # Project dependencies └── README.md # Project documentation

## Features

- **FastAPI Framework**: Modern, fast, and easy-to-use web framework for building APIs
- **SQLAlchemy ORM**: Database abstraction layer supporting multiple database engines
- **Database Support**: 
  - SQLite (default for development)
  - PostgreSQL, MySQL, and other SQL databases (production-ready)
- **Dependency Injection**: Context-aware database session management
- **RESTful API**: Clean and intuitive API endpoints for TODO management
- **Data Validation**: Pydantic schemas for request/response validation

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yagnesh-tendulkar/ITG-170-training.git
   cd ITG-170-training/TODO

   Code


## Features

- **FastAPI Framework**: Modern, fast, and easy-to-use web framework for building APIs
- **SQLAlchemy ORM**: Database abstraction layer supporting multiple database engines
- **Database Support**: 
  - SQLite (default for development)
  - PostgreSQL, MySQL, and other SQL databases (production-ready)
- **Dependency Injection**: Context-aware database session management
- **RESTful API**: Clean and intuitive API endpoints for TODO management
- **Data Validation**: Pydantic schemas for request/response validation

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yagnesh-tendulkar/ITG-170-training.git
   cd ITG-170-training/TODO

    Create a virtual environment:
    bash

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    Install dependencies:
    bash

    pip install -r requirements.txt

Configuration
Environment Variables

    DATABASE_URL: Database connection string
        Default: sqlite:///./todo_production.db
        Example PostgreSQL: postgresql://user:password@localhost/todo_db

Database Setup

The application automatically handles database initialization through SQLAlchemy's declarative base. On first run, all tables will be created.
Running the Application
bash

uvicorn app.main:app --reload

The API will be available at http://localhost:8000
API Documentation

    Swagger UI: http://localhost:8000/docs
    ReDoc: http://localhost:8000/redoc

API Endpoints
TODOs

    GET /todos/ - Retrieve all TODOs
    POST /todos/ - Create a new TODO
    GET /todos/{id} - Get a specific TODO
    PUT /todos/{id} - Update a TODO
    DELETE /todos/{id} - Delete a TODO

Technology Stack

    Backend Framework: FastAPI
    ORM: SQLAlchemy
    Database: SQLite (development) / PostgreSQL (production)
    Data Validation: Pydantic
    Server: Uvicorn

Development
Adding New Endpoints

    Create models in app/models/
    Define schemas in app/schemas/
    Create routes in app/routes/
    Import and include routers in app/main.py

Database Operations

Use the get_db() dependency to access the database session:
Python

from fastapi import Depends
from app.database.connection import get_db

@app.get("/todos/")
def get_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

Testing
bash

pytest tests/
