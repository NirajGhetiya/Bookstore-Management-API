from fastapi import FastAPI
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi import Depends
from database import SessionLocal
from database import engine
import models 
from Dto.dto import *
import Service.bookService as  bookService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{id:int}")
def book_by_id(id,db: Session = Depends(get_db) ):
    data=bookService.get_book_by_id(id,db)
    return data
    
@router.get("/")
def get_books(db:Session =Depends(get_db),pageNumber:int=1,pageSize:int=10):
    data = bookService.get_books(db,pageNumber,pageSize)
    return data

@router.post("/")
def create_book(book:BookDto,db:Session =Depends(get_db)):
   return  bookService.create_book(book,db)
     
@router.delete("/{id:int}")
def delete_book(id,db:Session=Depends(get_db)):
    return bookService.delete_book(id,db)     

@router.put("/{id:int}")
def update_book(id,book:BookDto,db:Session=Depends(get_db)):
    return bookService.update_book(id,book,db)

@router.get("/search/{title}")
def search_book(title,pageNumber:int=1,pageSize:int=10,db:Session=Depends(get_db)):
     return bookService.search_book(title,pageNumber,pageSize,db)
   