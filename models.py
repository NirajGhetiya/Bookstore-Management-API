from sqlalchemy import Boolean, Column,Float, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Book(Base):
    __tablename__ = "Books"

    id = Column(Integer, primary_key=True,autoincrement=True)
    title = Column(String)
    isbn = Column(String, unique=True)
    price= Column(String)
    author = Column(String)
    def __init__(self, title:str,isbn:str,price:str,author:str):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.author = author
