# from urllib import request
from fastapi import FastAPI # Depends, HTTPException, status, APIRouter
# from .schemas import CreateJobRequest
# from sqlalchemy.orm import Session
# from sqlalchemy import text, engine
# from .database import get_db, engine
from .routers import store, city
# from .models import Job


app = FastAPI()

app.include_router(store.router)
app.include_router(city.router)

@app.get("/")
def root():

    return {"message": "Welcome to a BreakingBad-production"}

# cat u05_schema.sql | psql -h localhost -U test-breakingbad -d bbdb


# @app.post("/")
# def create(details: CreateJobRequest, db: Session = Depends(get_db)):
#     to_create = Job(
#         title = details.title,
#         description = details.description
#     )
#     db.add(to_create)
#     db.commit()
#     return {
#         "success": True,
#         "created_id": to_create.id
#     }
# #  response_model=CreateJobRequest 
# @app.get("/")
# def get_posts(db: Session = Depends(get_db)):

#     posts = db.query(Job, Job.id, Job.title, Job.description).all()
#     # from_statement(text('''SELECT * FROM jobs;'''))
    
#     if not posts:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail="No posts was found")

#     return {"data": posts}