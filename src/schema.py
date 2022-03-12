from pydantic import BaseModel
from typing import Optional

class Stores(BaseModel):
    name: Optional[str]
    address: Optional[str]
    zip: Optional[str]
    city: Optional[str]