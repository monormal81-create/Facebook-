from sqlalchemy.orm import Session

from database.models import User
from database.models import Post


# =========================
# GET PROFILE
# =========================

def get_profile(db: Session, username: str):

    user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    if not user:
        raise ValueError("User not found")

    return user


# =========================
# USER POSTS
# =========================

def get_user_posts(db: Session, user_id: int):

    posts = (
        db.query(Post)
        .filter(Post.user_id == user_id)
        .order_by(Post.id.desc())
        .all()
    )

    return posts


# =========================
# PROFILE STATS (MVP)
# =========================

def get_profile_stats(db: Session, user_id: int):

    posts_count = (
        db.query(Post)
        .filter(Post.user_id == user_id)
        .count()
    )

    return {
        "posts_count": posts_count
    }