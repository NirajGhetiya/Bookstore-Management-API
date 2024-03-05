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

@router.get("/book/{id:int}")
def root(id,db: Session = Depends(get_db) ):
    data=bookService.get_book_by_id(id,db)
    return {"code":200, "status":"success","data":data}
    
@router.get("/books/")
def read_books(db:Session =Depends(get_db)):
    data = bookService.get_books(db)
    return{"code":200, "status":"success","data":data}

@router.post("/addBooks/")
def create_book(book:BookDto ,db:Session = Depends(get_db)):
   return  bookService.create_book(book,db)
     
@router.delete("/{id:int}")
def delete_book(id,db:Session=Depends(get_db)):
    return bookService.delete_book(id,db)     

@router.put("/updateBook/{id}")
def update_book(id,book:BookDto,db:Session=Depends(get_db)):
    return bookService.update_book(id,book,db)

@router.get("/search/{keyword}")
def search_book(keyword,db:Session=Depends(get_db)):
    data=bookService.search_book(keyword,db)
   