from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from config import models
from config.database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class UserBase(BaseModel):
    usernames: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
def read_root():
    return {"Hello": "World"}

# endpoint to store a username to the database
@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()

# endpoint to retrieve stored user information from database
@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: db_dependency):
    user = db.query(
        models.User
    ).filter(
        models.User.id == user_id
    ).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User ID is not found in the database!"
        )
    return user

# endpoint to store a post to the database
@app.post("/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase, db: db_dependency):
    db_post = models.Post(**post.model_dump())
    db.add(db_post)
    db.commit()

# endpoint to retrieve stored post data from database
@app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def get_post(post_id: int, db: db_dependency):
    post = db.query(
        models.Post
    ).filter(
        models.Post.id == post_id
    ).first()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Post ID is not found in the database!"
        )
    return post