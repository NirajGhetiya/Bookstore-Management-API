from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base
from main import app
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
    response = client.get("/book/books/")
    assert response.status_code == 200
    data = response.json()
    assert data["data"] == []
    assert data["status"] == "success"

def test_add_book():
    book_data = {
        "title": "Rich dad Poor dad",
        "isbn" : "123321123",
        "price": "150",
        "author" : "Robert Kiyosaki",  
    }
    response = client.post("/book/addBooks", json=book_data)
    assert response.status_code == 200