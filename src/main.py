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

@app.get("/", response_model=CreateJobRequest)
def get_posts(db: Session = Depends(get_db)):

    posts = db.query(Job).all()

    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No posts was not found")

    return {"data": posts}

