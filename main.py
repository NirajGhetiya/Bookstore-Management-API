from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi import Depends
from database import SessionLocal
from database import engine
from Controller.bookController import router

import models 
import Service.bookService as  bookService

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router, prefix="/book", tags=["book"])



