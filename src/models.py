import uuid
from sqlalchemy import VARCHAR, Integer, String
from sqlalchemy.sql.schema import Column
from .database import Base

#class Job(Base):
#    __tablename__ = "jobs"

#    id = Column(Integer, primary_key=True)
#    title = Column(String, nullable=False)
#    description = Column(String, nullable=False)

# class Stores(Base):
#     __tablename__ = "stores"

#     id = Column(uuid, primary_key=True, nullable=False)
#     name = Column(VARCHAR(50), nullable=False, unique=True)