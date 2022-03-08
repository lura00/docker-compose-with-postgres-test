from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy import VARCHAR
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix='/city',
    tags=['Cities']
)


@router.get("/")
def get_city(db: Session = Depends(get_db)):
    
    city = db.execute("SELECT city FROM store_addresses")

    if city == "":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details="No stores was found")

    return list(city)


@router.get("/{zip}")
def get_city(zip: int, db: Session = Depends(get_db)):
    
    city = db.execute(f"SELECT city FROM store_addresses WHERE zip = '{zip}'")

    if city == "":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details="No stores was found")

    return list(city)