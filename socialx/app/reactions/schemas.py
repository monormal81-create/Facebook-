from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# =========================
# LIKE
# =========================

class LikeCreate(BaseModel):
    post_id: int


# =========================
# COMMENT
# =========================

class CommentCreate(BaseModel):
    post_id: int
    content: str
    parent_id: Optional[int] = None


class CommentResponse(BaseModel):
    id: int
    user_id: int
    post_id: int
    content: str
    parent_id: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True