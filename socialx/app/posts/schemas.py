from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PostCreate(BaseModel):
    content: str
    image: Optional[str] = None


class PostResponse(BaseModel):
    id: int
    user_id: int
    content: str
    image: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True