from sqlalchemy.orm import Session
from models import Book
from Dto.dto import  *

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()
    
def get_book_by_isbn(db: Session, book_isbn: int):
    return db.query(Book).filter(Book.isbn == book_isbn).first()

def create_book(db: Session, book: Book):
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def update_book(db: Session,id:id, book: BookDto):
    book_db=db.query(Book).filter(Book.id == id).first()
    if book is None:
        return None
    book_db.isbn = book.isbn
    book_db.author= book.author
    book_db.title = book.title
    book_db.price = book.price
    db.commit()
    db.refresh(book_db)
    return book_db
    

def delete_book(db: Session, book_id: int):
    book = get_book_by_id(db, book_id)
    if book is None:
        return None
    db.delete(book)
    db.commit()
    return book