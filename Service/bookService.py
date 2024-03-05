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
       return None
    return book

def get_books(db: Session ):
    books =repository.get_books(db)
    return books

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


  

# def create_new_book(    request: Request) -> Response:
#     new_book = book_schema.load(json.loads(request.body.decode('utf-8')), session='create')
#     if new_book.errors:
#         return json_response({"status": "fail", "message": "Validation error", "data": new_book.errors}, status
#         return json_response({'errors': new_book.errors}, status=422)
#     else:
#         try:
#             repository.add_book(new_book.data)
#             return json_response(book_with_token_schema.dump(new_book.data), status=201)
#         except Exception as e:  
#             print("Error in adding a new book to the database")
#             print(e)
#             return json_response({"error": "Internal Server Error"}, status=500)
            

# def update_book(request: Request) -> Response:
#     id = int(request.match_info["id"])
#     data = json.loads(request.body.decode('utf-8'))
#     # Checking whether there are any changes made or not
#     if set(data.keys()) == {'index', 'title', 'author'} and all(v is None for v in data.    values()):
#         return json_response({'error':'No updates were provided.'},status=422)
#     book = repository.update_book(id, **data)
#     if not book:
#         return json_response({'error':'The specified book was not found.'},status=404)
