
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import User
from datetime import datetime
import bcrypt

router=APIRouter(prefix="/api/users", tags=["users"])

class UserCreate(BaseModel):
    name:str
    email:str
    role:str
    phone:str
    username:str
    password:str

@router.post("/register")
def register(data:UserCreate, db:Session=Depends(get_db)):
    if data.role not in ['BME','User','Manager']:
        return {'success':False,'message':'Invalid role selected'}
    hashed=bcrypt.hashpw(data.password.encode(), bcrypt.gensalt()).decode()
    user=User(name=data.name,email=data.email,role=data.role,
              department=data.role,phone=data.phone,
              username=data.username.lower().strip(),password_hash=hashed,
              created_at=datetime.now())
    db.add(user); db.commit(); db.refresh(user)
    return {"success":True,"message":"User registered successfully"}
