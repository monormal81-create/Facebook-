from sqlalchemy.orm import Session

from database.models import Like, Post

from app.realtime.manager import manager
import asyncio


# =========================
# LIKE POST
# =========================

def like_post(db: Session, post_id: int, user_id: int):
import time


class RateLimiter:

    def __init__(self):
        # user_id -> {action: last_time}
        self.user_actions = {}

    def is_allowed(self, user_id: int, action: str, limit_seconds: int = 5):

        now = time.time()

        if user_id not in self.user_actions:
            self.user_actions[user_id] = {}

        last_time = self.user_actions[user_id].get(action)

        if last_time:
            if now - last_time < limit_seconds:
                return False

        self.user_actions[user_id][action] = now
        return True


rate_limiter = RateLimiter()
if not rate_limiter.is_allowed(user_id, f"like_{post_id}", 3):
    return {"error": "Too many likes, slow down"}

    # التحقق إذا كان اللايك موجود
    existing_like = (
        db.query(Like)
        .filter(Like.post_id == post_id,
                Like.user_id == user_id)
        .first()
    )

    # إذا موجود نحذفه (unlike)
    if existing_like:
        db.delete(existing_like)
        db.commit()
        return {"message": "unliked"}

    # إنشاء لايك جديد
    like = Like(
        post_id=post_id,
        user_id=user_id
    )

    db.add(like)
    db.commit()
    db.refresh(like)

    # جلب صاحب المنشور
    post = db.query(Post).filter(Post.id == post_id).first()

    if post and post.user_id != user_id:

        # إرسال إشعار Real-time
        asyncio.create_task(
            manager.send_notification(
                post.user_id,
                {
                    "message": "أعجب شخص بمنشورك",
                    "type_action": "like",
                    "from_user_id": user_id,
                    "post_id": post_id
                }
            )
        )

    return like