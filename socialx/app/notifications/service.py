from sqlalchemy.orm import Session

from database.models import Notification


# =========================
# CREATE NOTIFICATION
# =========================

def create_notification(
    db: Session,
    user_id: int,
    from_user_id: int,
    type: str,
    message: str,
    post_id: int = None
):

    notification = Notification(
        user_id=user_id,
        from_user_id=from_user_id,
        type=type,
        message=message,
        post_id=post_id
    )

    db.add(notification)
    db.commit()
    db.refresh(notification)

    return notification


# =========================
# GET USER NOTIFICATIONS
# =========================

def get_notifications(db: Session, user_id: int):

    return (
        db.query(Notification)
        .filter(Notification.user_id == user_id)
        .order_by(Notification.id.desc())
        .all()
    )


# =========================
# MARK AS READ
# =========================

def mark_as_read(db: Session, notification_id: int):

    notif = (
        db.query(Notification)
        .filter(Notification.id == notification_id)
        .first()
    )

    if not notif:
        raise ValueError("Notification not found")

    notif.is_read = True

    db.commit()

    return notif
    from app.realtime.manager import manager
import asyncio


# =========================
# SEND NOTIFICATION REAL-TIME
# =========================

def send_notification(user_id: int, message: str, notif_type: str, from_user_id: int):

    asyncio.create_task(
        manager.send_notification(
            user_id,
            {
                "message": message,
                "type_action": notif_type,
                "from_user_id": from_user_id
            }
        )
    )