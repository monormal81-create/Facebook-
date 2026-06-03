from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    display_name: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    user_tag: str
    username: str
    display_name: str
    email: str
    bio: str
    avatar: str
    cover: str
    theme: str
    is_verified: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True