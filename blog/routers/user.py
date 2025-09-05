from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, hashing
from ..database import get_db
from .repository import user as userRepository
router = APIRouter(
   prefix="/user",
   tags = ['users']
)



@router.post('/' , response_model = schemas.ShowUser)
def create_user(request: schemas.User , db : Session = Depends(get_db)):
   return userRepository.create(request , db)
  
   
@router.get('/{id}' , response_model = schemas.ShowUser)
def get_user(id:int,db:Session = Depends(get_db)):
   return userRepository.show(id, db)
