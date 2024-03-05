from pydantic import BaseModel
from typing import List, Optional, Generic, TypeVar
from pydantic.generics import GenericModel
from models import Book
from pydantic import BaseModel 

class BookDto(BaseModel):
    title: str =" Book Title"
    isbn: str=  "123456789"
    price:str ="50.23"
    author:str
    class Config:
        orm_mode = True
class BookResponsDto(BaseModel):
    id:int
    title: str 
    isbn: str
    price:str
    author:str      
    