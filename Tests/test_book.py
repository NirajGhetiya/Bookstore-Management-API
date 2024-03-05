from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base
from app.main import app
from Controller.bookController import get_db


SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

def test_get_books():
    book_data = {
        "title": "Rich dad Poor dad",
        "isbn" : "12123321123",
        "price": "150",
        "author" : "Robert Kiyosaki",  
    }
    client.post("/book/addBooks", json=book_data)

    response = client.get("/book/books/")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 1

def test_add_book():
    book_data = {
        "title": "Rich dad Poor dad",
        "isbn" : "123321",
        "price": "150",
        "author" : "Robert Kiyosaki",  
    }
    response = client.post("/book/addBooks", json=book_data)
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 201
    assert data["data"] == {
        "price": "150",
        "title": "Rich dad Poor dad",
        "isbn" : "123321",
        "author" : "Robert Kiyosaki", 
        "id": 2
    }

def test_delete_book():
    response = client.delete("/book/2")
    assert response.status_code == 200
    data = response.json()
    assert data["msg"] == "Deleted Successfully"
    assert data["data"] == {
        "price": "150",
        "title": "Rich dad Poor dad",
        "isbn" : "123321",
        "author" : "Robert Kiyosaki", 
        "id": 2
    }

def test_update_book():
    book_data = {
        "title": "The Mastery",
        "isbn" : "123321",
        "price": "250",
        "author" : "Robert Greene",  
    }
    response = client.put("/book/updateBook/1", json=book_data)
    assert response.status_code == 200
    data = response.json()
    assert data["msg"] == "Updated Successfully"
    assert data["data"] == {
        "title": "The Mastery",
        "isbn" : "123321",
        "price": "250",
        "author" : "Robert Greene", 
        "id" : 1
    }

def test_search_book():
    response = client.get("/book/search/The Mastery")
    assert response.status_code == 200
    data = response.json()
    assert data["data"] == [{
        "title": "The Mastery",
        "isbn" : "123321",
        "price": "250",
        "author" : "Robert Greene", 
        "id" : 1
    }]