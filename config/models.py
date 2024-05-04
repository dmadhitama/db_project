from sqlalchemy import Column, Boolean, String, Integer, Float
from config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    usernames = Column(String(255), unique=True, nullable=False)
    
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    content = Column(String(255))
    user_id = Column(Integer)
