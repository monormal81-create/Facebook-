from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database.dependencies import get_db
from database.models import User

from app.auth.dependencies import get_current_user

from app.notifications.service import create_notification
from app.notifications.service import get_notifications
from app.notifications.service import mark_as_read
from app.notifications.schemas import NotificationResponse


router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


# =========================
# GET NOTIFICATIONS
# =========================

@router.get("/", response_model=list[NotificationResponse])
def list_notifications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_notifications(db, current_user.id)


# =========================
# MARK AS READ
# =========================

@router.post("/read/{notification_id}")
def read_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):

    try:
        return mark_as_read(db, notification_id)

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))