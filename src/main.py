from fastapi import FastAPI, Depends, HTTPException, status
from .schemas import CreateJobRequest
from sqlalchemy.orm import Session
from sqlalchemy import text
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
#  response_model=CreateJobRequest 
@app.get("/")
def get_posts(db: Session = Depends(get_db)):

    posts = db.query(Job, Job.id, Job.title, Job.description).all()
    # from_statement(text('''SELECT * FROM jobs;'''))
    
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No posts was found")

    return {"data": posts}


@app.get("/stores")
def get_stores(db: Session = Depends(get_db)):

    stores = db.query(text(" * FROM stores")).all() # This line prints out 5 empty rows. If I add "SELECT"
    # I get an error:  [SQL: SELECT SELECT * FROM stores]
    # u05-test-web-1  | (Background on this error at: https://sqlalche.me/e/14/f405)
    
    # result = db.execute(stores).all()

    # stores = db.query(Stores, Stores.id, Stores.name).all()

    if stores == "":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details="No stores was found")

    # for row in result:
    #     table_data = {row}
    #     # print(table_data)
    #     return table_data
    return stores
