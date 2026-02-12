# Learn FastAPI: From Basic to Advanced with Databases

This is a comprehensive learning project designed to teach FastAPI concepts from basic to advanced levels, with a focus on database integration and real-world application development.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Database Integration](#database-integration)
- [Advanced Concepts Covered](#advanced-concepts-covered)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project serves as a hands-on learning resource for developers wanting to master FastAPI, covering everything from basic routing to advanced database operations. The application implements CRUD operations for products and students, demonstrating real-world use cases with both in-memory data and MongoDB integration.

## Features

- RESTful API endpoints for products and students
- File upload functionality
- Data validation using Pydantic models
- Database integration with MongoDB
- Environment variable configuration
- Dependency injection
- Error handling
- Static file serving

## Project Structure

```
learn-fastapi/
├── app/
│   ├── __init__.py
│   ├── .env
│   ├── data/
│   │   ├── __init__.py
│   │   ├── data.py          # In-memory data storage
│   │   └── mongo.py         # MongoDB connection
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── product.py       # Product API endpoints
│   │   ├── practice.py      # File upload endpoints
│   │   └── student.py       # Student API endpoints
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── product.py       # Product Pydantic models
│   │   └── student.py       # Student Pydantic models
│   ├── services/
│   │   ├── __init__.py
│   │   └── product.py       # Product business logic
│   └── uploads/             # Directory for uploaded files
├── main.py                  # Main application entry point
├── pyproject.toml           # Project dependencies
├── README.md                # This file
└── .python-version
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd learn-fastapi
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
```bash
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
# Or if using pyproject.toml
pip install .
```

## Configuration

Create a `.env` file in the `app` directory with the following variables:

```env
DB_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/
DB_NAME=students_db
```

## API Endpoints

### Products API (`/Products`)
- `GET /Products` - Retrieve all products
- `POST /Products` - Create a new product

### Students API (`/students`)
- `GET /students` - Retrieve all students
- `POST /students` - Create a new student
- `GET /students/{name}` - Retrieve a student by name
- `PUT /students/{name}` - Update a student by name
- `DELETE /students/{name}` - Delete a student by name

### File Upload API (`/upload`)
- `POST /upload` - Upload a file with description

## Database Integration

The application demonstrates two approaches to data storage:

1. **In-Memory Storage**: Used for products in `app/data/data.py`
2. **MongoDB Integration**: Used for students in `app/data/mongo.py`

The MongoDB integration includes:
- Connection management
- Environment variable configuration
- Collection access abstraction
- Error handling

## Advanced Concepts Covered

This project teaches several advanced FastAPI concepts:

### 1. Pydantic Models
- Data validation and serialization
- Custom field validation
- Type hints and constraints

### 2. Dependency Injection
- Service layer separation
- Business logic encapsulation
- Reusable dependencies

### 3. API Router
- Modular endpoint organization
- Route grouping and prefixes
- Tagging for documentation

### 4. Request/Response Handling
- File uploads with metadata
- Form data processing
- Response model definitions

### 5. Error Handling
- HTTP exception raising
- Custom error responses
- Validation error handling

### 6. Static Files
- Serving uploaded files
- Static file mounting
- URL generation

## Running the Application

1. Ensure your virtual environment is activated
2. Make sure your MongoDB connection is configured in `.env`
3. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

The interactive API documentation will be available at:
- `http://127.0.0.1:8000/docs` (Swagger UI)
- `http://127.0.0.1:8000/redoc` (ReDoc)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.