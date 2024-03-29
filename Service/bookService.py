from Dto.dto import  *

from database import SessionLocal
from fastapi import Depends
from models import Book
import repository

from sqlalchemy.orm import Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def get_book_by_id(id:int) -> ApiResponseDto:
#     response = ApiResponseDto[Book]
#     book = repository.get_book_by_id(book_id=id, db=Depends(get_db))
#     if not book:
#         response.code = 404
#         response.message = "Not Found"
#         response.success = False
#     else:
#         response.code = 200
#         response.result=book
#     return response
    
def get_book_by_id(id:int,db: Session):
    
    book = repository.get_book_by_id(db,id)
    if not book:
       return {"code":404,"msg":"No such book found"}
    return {"code":200,"msg":"get Successfully", "data":book}

def get_books(db: Session ,pageNumber,pageSize ):
    data =repository.get_books(db)
    if len(data) is 0:
        return {"code":404,"msg":"No such book found"}
    return {"total":len(data),"per_page":pageSize,"current_page":pageNumber,"data":data[(pageNumber-1)*pageSize:((pageNumber-1)*pageSize)+pageSize]}

def create_book(book:BookDto,db:Session):
    book2 = repository.get_book_by_isbn(db,book.isbn)
    if book2 is not None:
        return {"code":401, "msg":"Isbn already exists"}
    new_book = Book(title=book.title,author=book.author,isbn=book.isbn,price=book.price)
    

    book_temp= repository.create_book(db,new_book)
    if book_temp is None:
        return {"code":500, "msg":"We apologize, but we encountered an error while attempting to add the book to our database. This could be due to technical issues or invalid data provided."}
    return {"code":201,"msg":"Created Successfully","data":new_book}

def delete_book(id: int ,db: Session):
    data = repository.delete_book(db, id)
    if data is None:
        return {"code":404,"msg":"No such book found"}
    
    return {"code":200,"msg":"Deleted Successfully", "data":data}

def update_book(id:id,book:BookDto,db:Session):
    book_db=repository.get_book_by_id(db,id)
    if book is None:
        return {"code":404,"msg":"No such book found"}
   
    data = repository.update_book(db,id,book)
    return {"code":200,"msg":"Updated Successfully" ,"data":data} 

def search_book(title:str,pageNumber,pageSize, db: Session):
    books = repository.get_books(db)
    query = title.lower()
    data = [book for book in books if query in book.title.lower()]
    if len(data) is 0:
        return {"code":404,"msg":"No such book found"}
    return {"total":len(data),"per_page":pageSize,"current_page":pageNumber,"data":data[(pageNumber-1)*pageSize:((pageNumber-1)*pageSize)+pageSize]}