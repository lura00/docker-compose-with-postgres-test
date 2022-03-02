from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import Field, BaseSettings

# class Settings(BaseSettings):
#     db_url: str = Field(..., env='DATABASE_URL')

# settings = Settings()
SQLALCHEMY_DATABASE_URL = "postgresql://test-breakingbad:testpass@db:5432/bbdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()