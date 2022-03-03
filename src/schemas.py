from pydantic import BaseModel

class CreateJobRequest(BaseModel):
    title: str
    description: str

    class config:
        orm_mode = True