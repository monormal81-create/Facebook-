from sqlalchemy.orm import Session

from database.models import User, Post


# =========================
# SEARCH USERS
# =========================

def search_users(db: Session, query: str):

    return (
        db.query(User)
        .filter(User.username.contains(query))
        .all()
    )


# =========================
# SEARCH POSTS
# =========================

def search_posts(db: Session, query: str):

    return (
        db.query(Post)
        .filter(Post.content.contains(query))
        .all()
    )


# =========================
# SEARCH HASHTAGS POSTS
# =========================

def search_hashtag(db: Session, tag: str):

    return (
        db.query(Post)
        .filter(Post.hashtags.contains(tag))
        .all()
    )