from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    content: str

class PostUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class NotFoundSchema(BaseModel):
    message: str