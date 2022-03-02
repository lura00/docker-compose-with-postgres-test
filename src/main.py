from fastapi import FastAPI, Depends, HTTPException, status
from .schemas import CreateJobRequest
from sqlalchemy.orm import Session
from .database import get_db
from .models import Job


app = FastAPI()

@app.post("/")
def create(details: CreateJobRequest, db: Session = Depends(get_db)):
    to_create = Job(
        title = details.title,
        description = details.description
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id": to_create.id
    }

