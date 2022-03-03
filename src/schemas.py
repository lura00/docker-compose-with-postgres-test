from pydantic import BaseModel

class CreateJobRequest(BaseModel):
    id: int
    title: str
    description: str

    class config:
        orm_mode = True