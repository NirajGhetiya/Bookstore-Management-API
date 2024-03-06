# Bookstore Management API with Python, FastAPI, Docker, and PostgreSQL

This project aims to replicate the functionalities of a provided Spring Boot project but using Python, FastAPI, Docker, and PostgreSQL.

## Project Goal

Develop a RESTful API for managing a bookstore inventory, utilizing Python, FastAPI, PostgreSQL, and Docker.

## Technologies Used

- **Programming Language:** Python
- **Web Framework:** FastAPI
- **Database:** PostgreSQL
- **Containerization:** Docker

## Features

### Book Entity

- **Attributes:** 
  - id (integer, primary key)
  - title (string)
  - author (string)
  - ISBN (string, unique)
  - price (float)

### API Endpoints

- `GET /books`: Retrieves a list of all books.
- `GET /books/{id}`: Retrieves a specific book by its ID.
- `GET /books/search?title={title}`: Searches for books by title (case-insensitive).
- `POST /books`: Adds a new book to the inventory.
- `PUT /books/{id}`: Updates an existing book.
- `DELETE /books/{id}`: Deletes a book from the inventory.

### Documentation

Integrate Swagger for API documentation with clear descriptions and examples for each endpoint.

## Project Structure

- `main.py`: Entry point for the application.
- `models.py`: Defines the Book model with its attributes.
- `database.py`: Handles database connection and management using SQLAlchemy.
- `repository.py`: Defines the BookRepository class with methods for CRUD operations on the Book entity.
- `service.py`: Encapsulates business logic and interacts with the repository.
- `api.py`: Defines the FastAPI application with endpoints for managing books.

## Development Steps

### Setup Environment

1. Install Python, FastAPI, Docker, and PostgreSQL.
2. Configure database connection details in `database.py`.

### Define Models

- Create the Book model in `models.py`.

### Database Access

- Utilize SQLAlchemy for database interaction in `database.py`.

### Repository Layer

- Develop the `BookRepository` class for CRUD operations (fetching, adding, updating, deleting) in `repository.py`.

### Service Layer

- Create the `BookService` class in `service.py` to handle business logic and interact with the repository.

### API Development

- Define the FastAPI application in `api.py`.
- Implement API endpoints using FastAPI routing and validation for user input.
- Link each endpoint with appropriate service logic.

### Documentation

- Integrate Swagger for API documentation, providing detailed descriptions and examples for each endpoint.

### Dockerization

- Create a `Dockerfile` to build and containerize the application.
- Specify the Python environment, dependencies, and project directory for execution within the container.

### Testing

- Implement unit and integration tests for the API and service layers.

## Deliverables

- Functional Python code for the API, including the specified features and documentation.
- A `Dockerfile` for containerizing the application.
- A `README.md` file with instructions on setting up, running, and testing the project.
