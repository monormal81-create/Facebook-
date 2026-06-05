from pydantic import BaseModel
from datetime import datetime


class NotificationResponse(BaseModel):
    id: int
    user_id: int
    from_user_id: int
    type: str
    post_id: int | None
    message: str
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True