from pydantic import BaseModel
from datetime import datetime


class ProfileResponse(BaseModel):
    id: int
    user_tag: str
    username: str
    display_name: str
    bio: str
    avatar: str
    cover: str
    theme: str
    is_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True