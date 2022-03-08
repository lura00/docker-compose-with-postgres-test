from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy import VARCHAR
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(
    prefix='/stores',
    tags=['Stores']
)


@router.get("/")
def get_stores(db: Session = Depends(get_db)):
    
    stores = db.execute("SELECT * FROM stores")

    if stores == "":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details="No stores was found")

    return list(stores)


@router.get("/{name}")
def get_store(name: str, db: Session = Depends(get_db)):
    
    store = db.execute(f"SELECT stores.name, store_addresses.address FROM stores JOIN store_addresses ON stores.id=store_addresses.store WHERE name='{name}'")

    if store == "":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details="No stores was found")

    return list(store)
