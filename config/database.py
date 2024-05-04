from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


userid = "testuser"
userpwd = "testpwd"
url = "localhost:5432/postgres"
DB_URL = f"postgresql+psycopg2://{userid}:{userpwd}@{url}"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

Base = declarative_base()
